import requests

from constants.urls import URL_GDS_DISTRICTS


def get_districts():
    return requests.get(URL_GDS_DISTRICTS).json()
