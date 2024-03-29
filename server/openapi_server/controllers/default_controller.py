import connexion
import six
from requests import HTTPError, RequestException

from openapi_server.models.component import Component  # noqa: E501
from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server import utils, logger

def create_component(overwrite):  # noqa: E501
    """Create a Component

    Creates a new instance of a &#x60;Component&#x60;. # noqa: E501

    :param component: A new &#x60;Component&#x60; to be created.
    :type component: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        try:
            logger.info("full path: {}".format(connexion.request.full_path))
            logger.info("request body: {}".format(connexion.request.get_json()))
            component = Component.from_dict(connexion.request.get_json())  # noqa: E501
            component_wings = utils.upload_wcm(component, overwrite)
            return component_wings
        except ValueError as err:
            logger.error("Value error", exc_info=True)
            return "Bad request: {}".format(err), 400, {}
        except HTTPError or RequestException as err:
            logger.error("HTTP error", exc_info=True)
            return "{}".format(err.args[0].reason), err.args[0].status_code, {}
        except Exception as err:
            logger.error("Exception error", exc_info=True)
            return "Internal Error: {}".format(err.args[0].reason), 500, {}
    return "Bad request", 400, {}


def create_dataset():  # noqa: E501
    """Create a Dataset

    Creates a new instance of a &#x60;Dataset&#x60;. # noqa: E501

    :param dataset: A new &#x60;Dataset&#x60; to be created.
    :type dataset: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        try:
            logger.info("full path: {}".format(connexion.request.full_path))
            logger.info("request body: {}".format(connexion.request.get_json()))
            dataset = Dataset.from_dict(connexion.request.get_json())  # noqa: E501
            dataset_wings = utils.upload_wcm_dataset(dataset)
            return dataset_wings
        except ValueError as err:
            return "Bad request: {}".format(err), 400, {}
        except HTTPError or RequestException as err:
            return "{}".format(err.args[0].reason), err.args[0].status_code, {}
        except Exception as err:
            return "Internal Error: {}".format(err.args[0].reason), 500, {}
    return "Bad request", 400, {}
