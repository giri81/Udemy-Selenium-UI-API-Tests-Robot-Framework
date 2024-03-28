# api_helpers.py

import requests


def authenticate_api(username, password):
    return requests.auth.HTTPDigestAuth(username, password)
