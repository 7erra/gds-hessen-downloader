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


def _get_downloads(uri: str, page: int = 1):
    response = requests.get(f"{uri}&page={page}")
    response.raise_for_status()

    json = response.json()

    paging = json["searchresult"]["paging"]
    pageSize = paging["pageSize"]
    total = paging["total"]
    downloads: list = json["searchresult"]["downloads"]

    if pageSize * page < total:
        downloads += _get_downloads(uri, page + 1)

    return downloads


def get_muncipalities(uri: str):
    downloads = _get_downloads(uri)
    return [Muncipality(x["name"], x["downloadLink"]["uri"]) for x in downloads]
