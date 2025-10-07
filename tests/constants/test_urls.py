import pytest
from constants.urls import RE_URL_GDS_MUNCIPALITY, URL_GDS_BASE, URL_GDS_DISTRICTS


@pytest.mark.parametrize(
    "url",
    [
        "https://gds.hessen.de/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FHochtaunuskreis",
        "https://gds.hessen.de/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLahn-Dill-Kreis",
        "https://gds.hessen.de/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLandkreis+Bergstra%C3%9Fe",
    ],
)
def test_regex_gds_muncipality(url):
    assert (RE_URL_GDS_MUNCIPALITY.match(url)) is not None


@pytest.mark.parametrize("url", [URL_GDS_BASE, URL_GDS_DISTRICTS])
def test_regex_does_not_match_base_urls(url):
    assert (RE_URL_GDS_MUNCIPALITY.match(url)) is None
