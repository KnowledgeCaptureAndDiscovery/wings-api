
from zipfile import ZipFile
import tempfile
import requests
import os
from wcm import _component, _utils
import wings
from openapi_server import logger
ignore_dirs = ["__MACOSX"]

def download_extract_zip(url, dir):
    temp = tempfile.NamedTemporaryFile(prefix="component_")
    content = download_file(url)
    temp.write(content)
    with ZipFile(temp.name, 'r') as zip:
        zip.extractall(dir)
    directories = os.listdir(dir)
    if isinstance(directories, list):
        try:
            for ignore_dir in ignore_dirs:
                directories.remove(ignore_dir)
        except:
            pass

    if len(directories) == 1:
        return os.path.join(dir, directories[0])
    else:
        raise ValueError("The zipfile must has one directory.")


def download_file(url):
    r = requests.get(url, allow_redirects=True)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError(r)
    except requests.exceptions.RequestException:
        raise requests.exceptions.RequestException(r)
    return r.content


def download_data_file(url, dir):
    filename = url.split('/')[-1]
    filepath = os.path.join(dir, filename)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
    return filepath


def obtain_link(model_catalog_uri):
    return model_catalog_uri


def upload_wcm(component, overwrite):
    model_catalog_url = component.model_catalog_uri
    wings_instance = component.wings_instance.to_dict()
    component_url = obtain_link(model_catalog_url)
    with tempfile.TemporaryDirectory(prefix="component") as dir:
        component_dir = download_extract_zip(component_url, dir)
        try:
            component = _component.deploy_component(component_dir, creds=wings_instance, overwrite=overwrite)
            return component
        except Exception as err:
            raise err


def upload_wcm_dataset(dataset):
    wings_instance = wings.init(**dataset.wings_instance.to_dict())

    data_type = dataset.type
    data_catalog_id = dataset.data_catalog_id
    url = dataset.url
    metadata_properties_data_type = {"data_catalog_id": "string"}
    metadata_properties_data = {"data_catalog_id": data_catalog_id}
    try:
        wings_instance.data.new_data_type(data_type, None)
        wings_instance.data.add_type_properties(data_type, properties=metadata_properties_data_type)

        with tempfile.TemporaryDirectory(prefix="data_") as dir:
            data_file = download_data_file(url, dir)
            data_id = wings_instance.data.upload_data_for_type(data_file, data_type)
            wings_instance.data.save_metadata(data_id, metadata_properties_data)
            return {"data_id": wings_instance.data.get_data_id(data_id)}
    except Exception as err:
        raise err
    finally:
        wings_instance.logout()
