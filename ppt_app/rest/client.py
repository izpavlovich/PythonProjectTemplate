import exceptions
import requests


class BaseClient(object):
    """
    Base REST Client class. Use this class as super
    class for specific endpoint clients.
    """

    def __init__(self, baseurl, entity):
        """
        Base constructor. It creates endpoint client with
        URL like baseurl/entity
        @param baseurl: Static part of the entity URL
        @param entity: Entity specific part of the URL
        """
        self.entity = entity
        self.baseurl = baseurl
        self.fullurl = self.baseurl + "/" + self.entity
        self.headers = {"content-type": "application/json",
                        "accept": "application/json"}

    def get(self):
        """Performes HTTP GET Request"""
        response = requests.get(self.fullurl,
                                headers=self.headers)
        return self._checkResponse(response, [200])

    def post(self, payload):
        """
        Performes HTTP POST Request
        @param payload: Data to be send inside the request's body
        """
        response = requests.post(self.fullurl,
                                 headers=self.headers,
                                 data=payload)
        return self._checkResponse(response,
                                   [200, 201, 204])

    def put(self, payload):
        response = requests.put(self.fullurl,
                                headers=self.headers,
                                payload=payload)
        return self._checkResponse(response,
                                   [200, 204])

    def delete(self):
        response = requests.delete(self.fullurl,
                                   headers=self.headers)
        return self._checkResponse(response,
                                   [200, 202, 204])

    def _validateResponseType(self, contentType):
        if contentType.startswith("application/json"):
            return True
        else:
            return False

    def _checkResponse(self, response, allowedCodes):
        if response.status_code not in allowedCodes:
            raise exceptions.ApiError("{} /{}/ {} {} {}".format(
                response.request.method,
                self.entity,
                response.status_code,
                "Unexpected status code returned for this operation. \
                Expected status codes are: ",
                allowedCodes))

        # Empty response HTTP204
        if response.status_code == 204:
            return None

        if not self._validateResponseType(response.headers['Content-Type']):
            raise exceptions.ApiError("{} /{}/ {} {} {}".format(
                response.request.method,
                self.entity,
                response.status_code,
                "Response is not JSON content-type. Actual content-type: ",
                response.headers['Content-Type']))

        return response


class TicketClient(BaseClient):
    """description of class"""

    def __init__(self, baseurl):
        return super(TicketClient, self).__init__(baseurl, "posts")
