# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Dataset(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, type=None, url=None, wings_instance=None):  # noqa: E501
        """Dataset - a model defined in OpenAPI

        :param id: The id of this Dataset.  # noqa: E501
        :type id: str
        :param type: The type of this Dataset.  # noqa: E501
        :type type: object
        :param url: The url of this Dataset.  # noqa: E501
        :type url: object
        :param wings_instance: The wings_instance of this Dataset.  # noqa: E501
        :type wings_instance: object
        """
        self.openapi_types = {
            'id': str,
            'type': object,
            'url': object,
            'wings_instance': object
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'url': 'url',
            'wings_instance': 'wings_instance'
        }

        self._id = id
        self._type = type
        self._url = url
        self._wings_instance = wings_instance

    @classmethod
    def from_dict(cls, dikt) -> 'Dataset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dataset of this Dataset.  # noqa: E501
        :rtype: Dataset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Dataset.


        :return: The id of this Dataset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dataset.


        :param id: The id of this Dataset.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Dataset.


        :return: The type of this Dataset.
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Dataset.


        :param type: The type of this Dataset.
        :type type: object
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this Dataset.


        :return: The url of this Dataset.
        :rtype: object
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Dataset.


        :param url: The url of this Dataset.
        :type url: object
        """

        self._url = url

    @property
    def wings_instance(self):
        """Gets the wings_instance of this Dataset.


        :return: The wings_instance of this Dataset.
        :rtype: object
        """
        return self._wings_instance

    @wings_instance.setter
    def wings_instance(self, wings_instance):
        """Sets the wings_instance of this Dataset.


        :param wings_instance: The wings_instance of this Dataset.
        :type wings_instance: object
        """
        if wings_instance is None:
            raise ValueError("Invalid value for `wings_instance`, must not be `None`")  # noqa: E501

        self._wings_instance = wings_instance
