from constants.urls import URL_GDS_DISTRICTS
from gds.districts import get_districts


def test_get_districts(requests_mock):
    response = {"test": "ok"}
    requests_mock.get(URL_GDS_DISTRICTS, json=response)

    result = get_districts()

    assert result == response
