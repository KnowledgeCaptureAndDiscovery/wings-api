
from zipfile import ZipFile
import tempfile
import requests
import os
from wcm import _component, _utils
import wings

def download_extract_zip(url, dir):
    temp = tempfile.NamedTemporaryFile(prefix="component_")
    content = download_file(temp, url)
    temp.write(content)
    with ZipFile(temp.name, 'r') as zip:
        zip.extractall(dir)
    list = os.listdir(dir)
    list.remove("__MACOSX")
    if len(list) == 1:
        return os.path.join(dir, list[0])
    else:
        raise ValueError("The zipfile must has one directory.")


def download_file(temp, url):
    r = requests.get(url, allow_redirects=True)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError(r)
    except requests.exceptions.RequestException:
        raise requests.exceptions.RequestException(r)
    return r.content


def obtain_link(model_catalog_uri):
    return model_catalog_uri


def upload_wcm(component):
    model_catalog_url = component.model_catalog_uri
    wings_instance = component.wings_instance
    mapping = {
        "domain": wings_instance.domain,
        "export_url": wings_instance.export_url,
        "password": wings_instance.password,
        "server": wings_instance.server,
        "username": wings_instance.username
    }
    component_url = obtain_link(model_catalog_url)
    with tempfile.TemporaryDirectory(prefix="component") as dir:
        component_dir = download_extract_zip(component_url, dir)
        try:
            return _component.deploy_component(component_dir, creds=mapping)
        except Exception as err:
            raise err


def upload_wcm_dataset(dataset):
    wings_data = dataset.wings_instance
    mapping = {
        "domain": wings_data.domain,
        "export_url": wings_data.export_url,
        "password": wings_data.password,
        "server": wings_data.server,
        "username": wings_data.username
    }
    wings_instance = wings.init(**mapping)

    data_type = dataset.type
    data_catalog_id = dataset.data_catalog_id
    url = dataset.url
    metadata_properties_data_type = {"data_catalog_id": "string"}
    metadata_properties_data = {"data_catalog_id": data_catalog_id}

    wings_instance.data.new_data_type(data_type, None)
    wings_instance.data.add_type_properties(data_type, properties=metadata_properties_data_type)

    temp = tempfile.NamedTemporaryFile(prefix="data_")
    download_file(temp, url)

    data_id = wings_instance.data.upload_data_for_type(temp.name, data_type)
    wings_instance.data.save_metadata(data_id, metadata_properties_data)
