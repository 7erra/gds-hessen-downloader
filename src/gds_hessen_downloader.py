import sys
from gds.districts import get_districts
from download import download
from gds.muncipalities import get_muncipalities
from constants.urls import URL_GDS_BASE
from urllib.parse import quote


def main(download_dir: str):
    for district in get_districts():
        district_print_message = f"### Downloading district {district.name} ###"
        print("#" * len(district_print_message))
        print(district_print_message)
        print("#" * len(district_print_message))
        for muncipality in get_muncipalities(f"{URL_GDS_BASE}/{district.uri}"):
            download(
                f"{URL_GDS_BASE}{quote(muncipality.uri)}",
                f"{download_dir}/{muncipality.name}.zip",
            )


if __name__ == "__main__":
    _, download_dir = sys.argv
    main(download_dir)
