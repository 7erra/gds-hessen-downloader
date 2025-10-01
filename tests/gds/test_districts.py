from constants.urls import URL_GDS_DISTRICTS
from gds.districts import get_districts
from ..data.gds import test_gds_districts_response


def test_get_districts(requests_mock):
    response = test_gds_districts_response
    requests_mock.get(URL_GDS_DISTRICTS, json=response)

    result = get_districts()

    assert result == [
        "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FHochtaunuskreis",
        "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLahn-Dill-Kreis",
    ]
