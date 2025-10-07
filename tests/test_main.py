from constants.urls import RE_URL_GDS_MUNCIPALITY, URL_GDS_DISTRICTS
from gds_hessen_downloader import main

from .data.gds import test_gds_districts_response, test_get_muncipalities_response

expected_calls = [
    (
        "https://gds.hessen.de/downloadcenter/20251001/3D-Daten/Digitales%20Gel%C3%A4ndemodell%20%28DGM1%29/Hochtaunuskreis/Bad%20Homburg%20v.d.H%C3%B6he%20-%20DGM1.zip",
        "download/Bad Homburg v.d.Höhe - DGM1.zip",
    ),
    (
        "https://gds.hessen.de/downloadcenter/20251001/3D-Daten/Digitales%20Gel%C3%A4ndemodell%20%28DGM1%29/Hochtaunuskreis/Friedrichsdorf%20-%20DGM1.zip",
        "download/Friedrichsdorf - DGM1.zip",
    ),
] * 2


def test_main(requests_mock, mocker):
    requests_mock.get(URL_GDS_DISTRICTS, json=test_gds_districts_response)
    requests_mock.get(RE_URL_GDS_MUNCIPALITY, json=test_get_muncipalities_response)
    mocked_download = mocker.patch("gds_hessen_downloader.download")

    main("download")

    mocked_download.assert_has_calls([mocker.call(*x) for x in expected_calls])


def test_download_failed(requests_mock, mocker):
    requests_mock.get(URL_GDS_DISTRICTS, json=test_gds_districts_response)
    requests_mock.get(RE_URL_GDS_MUNCIPALITY, json=test_get_muncipalities_response)
    mocked_download = mocker.patch(
        "gds_hessen_downloader.download", side_effect=RuntimeError("Runtime Error")
    )

    main("download")

    mocked_download.assert_has_calls([mocker.call(*x) for x in expected_calls])
