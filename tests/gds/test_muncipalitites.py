from src.gds.muncipalities import Muncipality, get_muncipalities
from ..data.gds import (
    test_get_muncipalities_response,
    test_get_muncipalities_response_with_paging,
    test_get_muncipalities_response_with_paging_page2,
)


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


def test_get_muncipalities_paging(requests_mock):
    uri = "https://gds.hessen.de/INTERSHOP/web/WFS/HLBG-Geodaten-Site/de_DE/-/EUR/ViewDownloadcenter-Start?path=3D-Daten/Digitales%20Gel%C3%A4ndemodell%20(DGM1)/Landkreis%20Kassel"

    uri_page2 = "https://gds.hessen.de/INTERSHOP/web/WFS/HLBG-Geodaten-Site/de_DE/-/EUR/ViewDownloadcenter-Start?path=3D-Daten/Digitales%20Gel%C3%A4ndemodell%20(DGM1)/Landkreis%20Kassel&page=2"

    requests_mock.get(uri, json=test_get_muncipalities_response_with_paging)
    requests_mock.get(uri_page2, json=test_get_muncipalities_response_with_paging_page2)

    result = get_muncipalities(uri)

    assert (
        Muncipality(
            "Fuldatal - DGM1",
            "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Fuldatal - DGM1.zip",
        )
        in result
    )
    assert (
        Muncipality(
            "Vellmar - DGM1",
            "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Vellmar - DGM1.zip",
        )
        in result
    )
