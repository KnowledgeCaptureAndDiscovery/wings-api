
from zipfile import ZipFile
import tempfile
import requests
import os
from wcm import _component, _utils


def download_extract_zip(url, dir):
    temp = tempfile.NamedTemporaryFile(prefix="component_")
    r = requests.get(url, allow_redirects=True)
    temp.write(r.content)
    with ZipFile(temp.name, 'r') as zip:
        zip.extractall(dir)

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
        component_dir = os.path.join(dir, component.id)
        try:
            return _component.deploy_component(component_dir, creds=mapping)
        except Exception as err:
            raise err
