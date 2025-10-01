import requests

from constants.urls import URL_GDS_DISTRICTS


def get_districts():
    response = requests.get(URL_GDS_DISTRICTS)
    response.raise_for_status()
    navigation = response.json()["navigation"]
    return [x["uri"] for x in navigation]
