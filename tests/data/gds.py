test_gds_districts_response = {
    "breadcrumb": [
        {
            "name": "Downloadcenter",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter",
        },
        {
            "name": "3D-Daten",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten&navigation=all",
        },
        {
            "name": "Digitales Geländemodell (DGM1)",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29&navigation=all",
        },
    ],
    "navigation": [
        {
            "name": "Hochtaunuskreis",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FHochtaunuskreis",
            "id": "DC0100058",
            "level": 3,
            "selected": False,
            "parentId": "DC0100057",
        },
        {
            "name": "Lahn-Dill-Kreis",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLahn-Dill-Kreis",
            "id": "DC0100059",
            "level": 3,
            "selected": False,
            "parentId": "DC0100057",
        },
    ],
    "searchresult": {
        "packages": [],
        "product": {
            "name": "Digitales Geländemodell (DGM1)",
            "id": "DC0100057",
            "description": "Beschreibung",
        },
        "downloads": [],
        "paging": {
            "total": 0,
            "pageSize": 20,
            "page": 1,
            "url": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29",
        },
    },
}

test_get_muncipalities_response = {
    "breadcrumb": [
        {
            "name": "Downloadcenter",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter",
        },
        {
            "name": "3D-Daten",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten&navigation=all",
        },
        {
            "name": "Digitales Geländemodell (DGM1)",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29&navigation=all",
        },
        {
            "name": "Hochtaunuskreis",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FHochtaunuskreis&navigation=all",
        },
    ],
    "navigation": [],
    "searchresult": {
        "packages": [],
        "product": {
            "name": "Hochtaunuskreis",
            "id": "DC0100058",
            "description": '<b>Digitales Geländemodell (DGM1)</b><br><br>Höhenmäßige Beschreibung des Geländereliefs durch räumliche Repräsentanten in Rasterform (Pixel) mit der quadratischen Fläche von 1 m * 1 m (1 Quadratmeter). Der originäre Höhenbezug ist die Rastermitte. Weitere Informationen zum DGM1 finden Sie <a href="https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle" target="_blank">hier</a>.<ul><i><b>Downloads:</b></i><li><a href="/INTERSHOP/static/WFS/HLBG-Geodaten-Site/-/HLBG-Geodaten/de_DE/Downloadcenter/Daten/3D-Daten/Aktualität_3D_0.pdf" target="_blank">Aktualitätsübersicht DGM1 und DOM1</a></b></i><li><a href="/INTERSHOP/static/WFS/HLBG-Geodaten-Site/-/HLBG-Geodaten/de_DE/Downloadcenter/Daten/3D-Daten/metadatenliste.pdf" target="_blank">metadatenliste</a></li></ul>',
        },
        "downloads": [
            {
                "name": "Bad Homburg v.d.Höhe - DGM1",
                "id": "DP0100903",
                "fileExtension": "ZIP",
                "fileSize": "159,2 MB",
                "creationDate": "12.06.2025",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251001/3D-Daten/Digitales Geländemodell (DGM1)/Hochtaunuskreis/Bad Homburg v.d.Höhe - DGM1.zip",
                },
            },
            {
                "name": "Friedrichsdorf - DGM1",
                "id": "DP0100904",
                "fileExtension": "ZIP",
                "fileSize": "94,6 MB",
                "creationDate": "12.06.2025",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251001/3D-Daten/Digitales Geländemodell (DGM1)/Hochtaunuskreis/Friedrichsdorf - DGM1.zip",
                },
            },
        ],
        "paging": {
            "total": 13,
            "pageSize": 20,
            "page": 1,
            "url": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FHochtaunuskreis",
        },
    },
}
