import re


URL_GDS_BASE = "https://gds.hessen.de"
URL_GDS_DISTRICTS = f"{URL_GDS_BASE}/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29"

RE_URL_GDS_MUNCIPALITY = re.compile(f"{re.escape(URL_GDS_DISTRICTS)}%2F.+")
