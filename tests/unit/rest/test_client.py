from tests.unit import test
# from mock import patch
# import requests
import requests_mock
import ppt_app.rest.client as client
import inspect


class BaseClient(test.TestCase):
    """Unit tests for Base Rest Client"""

    def setUp(self):
        return super(BaseClient, self).setUp()

    def _test_method(self, mock, method, expected_status_code):
        mock.register_uri(str.upper(method),
                          "mock://test.com/entity",
                          status_code=expected_status_code,
                          json={"data": "data"},
                          headers={"Content-Type": "application/json"})

        c = client.BaseClient("mock://test.com", "entity")

        methodToCall = getattr(c, method)

        hasData = hasattr(inspect.getargspec(methodToCall), 'args')

        if hasData:
            response = methodToCall(c)
        else:
            response = methodToCall(c, {"data": "data"})

        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual({"data": "data"}, response.json())

    def test__init__(self):
        c = client.BaseClient("base", "entity")
        self.assertEqual("base", c.baseurl)
        self.assertEqual("entity", c.entity)
        self.assertEqual("base/entity", c.fullurl)
        self.assertEqual({"content-type": "application/json",
                          "accept": "application/json"},
                         c.headers)

    @requests_mock.mock()
    def test_get(self, m):
        m.register_uri("GET",
                       "mock://test.com/entity",
                       status_code=200,
                       json={"data": "data"},
                       headers={"Content-Type": "application/json"})

        c = client.BaseClient("mock://test.com", "entity")
        response = c.get()

        self.assertEqual(200, response.status_code)
        self.assertEqual({"data": "data"}, response.json())

    @requests_mock.mock()
    def test_post(self, m):
        self._test_method(m, "post", 201)

    def test_put(self):
        self.assertIsNot(2, 31)

    def test_delete(self):
        self.assertIsNot(2, 31)
