# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.wings_instance import WingsInstance
from openapi_server import util

from openapi_server.models.wings_instance import WingsInstance  # noqa: E501

class Component(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, model_catalog_uri=None, wings_instance=None):  # noqa: E501
        """Component - a model defined in OpenAPI

        :param id: The id of this Component.  # noqa: E501
        :type id: str
        :param model_catalog_uri: The model_catalog_uri of this Component.  # noqa: E501
        :type model_catalog_uri: str
        :param wings_instance: The wings_instance of this Component.  # noqa: E501
        :type wings_instance: WingsInstance
        """
        self.openapi_types = {
            'id': str,
            'model_catalog_uri': str,
            'wings_instance': WingsInstance
        }

        self.attribute_map = {
            'id': 'id',
            'model_catalog_uri': 'model_catalog_uri',
            'wings_instance': 'wings_instance'
        }

        self._id = id
        self._model_catalog_uri = model_catalog_uri
        self._wings_instance = wings_instance

    @classmethod
    def from_dict(cls, dikt) -> 'Component':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Component of this Component.  # noqa: E501
        :rtype: Component
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Component.

        The component id  # noqa: E501

        :return: The id of this Component.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Component.

        The component id  # noqa: E501

        :param id: The id of this Component.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def model_catalog_uri(self):
        """Gets the model_catalog_uri of this Component.

        The model catalog id  # noqa: E501

        :return: The model_catalog_uri of this Component.
        :rtype: str
        """
        return self._model_catalog_uri

    @model_catalog_uri.setter
    def model_catalog_uri(self, model_catalog_uri):
        """Sets the model_catalog_uri of this Component.

        The model catalog id  # noqa: E501

        :param model_catalog_uri: The model_catalog_uri of this Component.
        :type model_catalog_uri: str
        """

        self._model_catalog_uri = model_catalog_uri

    @property
    def wings_instance(self):
        """Gets the wings_instance of this Component.


        :return: The wings_instance of this Component.
        :rtype: WingsInstance
        """
        return self._wings_instance

    @wings_instance.setter
    def wings_instance(self, wings_instance):
        """Sets the wings_instance of this Component.


        :param wings_instance: The wings_instance of this Component.
        :type wings_instance: WingsInstance
        """

        self._wings_instance = wings_instance
