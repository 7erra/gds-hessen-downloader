from src.gds.muncipalities import Muncipality, get_muncipalities
from ..data.gds import test_get_muncipalities_response


def test_get_muncipalities(requests_mock):
    uri = "https://gds.hessen.de/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FHochtaunuskreis"
    requests_mock.get(uri, json=test_get_muncipalities_response)

    result = get_muncipalities(uri)

    assert result == [
        Muncipality(
            "Bad Homburg v.d.Höhe - DGM1",
            "/downloadcenter/20251001/3D-Daten/Digitales Geländemodell (DGM1)/Hochtaunuskreis/Bad Homburg v.d.Höhe - DGM1.zip",
        ),
        Muncipality(
            "Friedrichsdorf - DGM1",
            "/downloadcenter/20251001/3D-Daten/Digitales Geländemodell (DGM1)/Hochtaunuskreis/Friedrichsdorf - DGM1.zip",
        ),
    ]
