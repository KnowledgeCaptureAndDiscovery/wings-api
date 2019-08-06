# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.component import Component  # noqa: E501
from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_component(self):
        """Test case for create_component

        Create a Component
        """
        component = {
  "wings_instance" : {
    "password" : "",
    "domain" : "",
    "export_url" : "",
    "server_url" : "",
    "user" : ""
  },
  "id" : "id"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/components',
            method='POST',
            headers=headers,
            data=json.dumps(component),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_dataset(self):
        """Test case for create_dataset

        Create a Dataset
        """
        dataset = {
  "wings_instance" : "",
  "id" : "id",
  "type" : "",
  "url" : ""
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/datasets',
            method='POST',
            headers=headers,
            data=json.dumps(dataset),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getdatasets(self):
        """Test case for getdatasets

        List All datasets
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/datasets',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
