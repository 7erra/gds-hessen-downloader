import requests


class Muncipality:
    name: str
    uri: str

    def __init__(self, name: str, uri: str) -> None:
        self.name = name
        self.uri = uri

    def __eq__(self, other: object, /) -> bool:
        return (
            isinstance(other, Muncipality)
            and self.name == other.name
            and self.uri == other.uri
        )


def get_muncipalities(uri: str):
    response = requests.get(uri)
    response.raise_for_status()
    downloads = response.json()["searchresult"]["downloads"]
    return [Muncipality(x["name"], x["downloadLink"]["uri"]) for x in downloads]
