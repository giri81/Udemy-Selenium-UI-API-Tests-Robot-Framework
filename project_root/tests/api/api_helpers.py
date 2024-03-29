# api_helpers.py

from requests.auth import HTTPBasicAuth


def authenticate_api(username, password):
    return HTTPDigestAuth(username, password)
