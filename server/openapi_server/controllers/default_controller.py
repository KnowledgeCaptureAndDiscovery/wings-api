import connexion
import six

from openapi_server.models.component import Component  # noqa: E501
from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.error import Error
from openapi_server import utils

def create_component():  # noqa: E501
    """Create a Component

    Creates a new instance of a &#x60;Component&#x60;. # noqa: E501

    :param component: A new &#x60;Component&#x60; to be created.
    :type component: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        try:
            component = Component.from_dict(connexion.request.get_json())  # noqa: E501
            component_wings = utils.upload_wcm(component)
            return component_wings
        except Exception as err:
            return "Internal Error: {}".format(err), 500, {}
    return "Bad request", 400, {}


def create_dataset():  # noqa: E501
    """Create a Dataset

    Creates a new instance of a &#x60;Dataset&#x60;. # noqa: E501

    :param dataset: A new &#x60;Dataset&#x60; to be created.
    :type dataset: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dataset = Dataset.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
