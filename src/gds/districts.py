import requests

from constants.urls import URL_GDS_DISTRICTS


def get_districts():
    return [x["uri"] for x in requests.get(URL_GDS_DISTRICTS).json()["navigation"]]
