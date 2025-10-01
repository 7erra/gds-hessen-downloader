import requests

from constants.urls import URL_GDS_DISTRICTS


class District:
    name: str
    uri: str

    def __init__(self, name: str, uri: str) -> None:
        self.name = name
        self.uri = uri

    def __eq__(self, other: object, /) -> bool:
        return (
            isinstance(other, District)
            and self.name == other.name
            and self.uri == other.uri
        )


def get_districts() -> list[District]:
    response = requests.get(URL_GDS_DISTRICTS)
    response.raise_for_status()
    navigation = response.json()["navigation"]
    return [District(x["name"], x["uri"]) for x in navigation]
