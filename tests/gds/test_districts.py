import pytest
from requests import HTTPError
from constants.urls import URL_GDS_DISTRICTS
from gds.districts import get_districts
from ..data.gds import test_gds_districts_response


def test_get_districts(requests_mock):
    requests_mock.get(URL_GDS_DISTRICTS, json=test_gds_districts_response)

    result = get_districts()

    assert result == [
        "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FHochtaunuskreis",
        "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLahn-Dill-Kreis",
    ]


def test_handle_invalid_response(requests_mock):
    requests_mock.get(
        URL_GDS_DISTRICTS, status_code=500, json={"message": "Internal Server Error"}
    )

    with pytest.raises(HTTPError, match="500 Server Error"):
        get_districts()
