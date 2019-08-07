
from zipfile import ZipFile
import tempfile
import requests
import os
from wcm import _component, _utils


def download_extract_zip(url, dir):
    temp = tempfile.NamedTemporaryFile(prefix="component_")
    r = requests.get(url, allow_redirects=True)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError(r)
    except requests.exceptions.RequestException:
        raise requests.exceptions.RequestException(r)

    temp.write(r.content)
    with ZipFile(temp.name, 'r') as zip:
        try:
            zip.extractall(dir)
        except:
            raise ValueError("format error")


def obtain_link(model_catalog_uri):
    return model_catalog_uri


def upload_wcm(component):
    model_catalog_url = component.model_catalog_uri
    wings_instance = component.wings_instance
    component_url = obtain_link(model_catalog_url)
    with tempfile.TemporaryDirectory(prefix="component") as dir:
        download_extract_zip(component_url, dir)
        mapping = {
            "domain": wings_instance.domain,
            "export_url": wings_instance.export_url,
            "password": wings_instance.password,
            "server": wings_instance.server,
            "username": wings_instance.username
        }
        if len(os.listdir(dir)) == 1:
            component_dir = os.path.join(dir, os.listdir(dir)[0])
            try:
                return _component.deploy_component(component_dir, creds=mapping)
            except Exception as err:
                raise err
        else:
            raise ValueError("Zipfile must contains one directory")

