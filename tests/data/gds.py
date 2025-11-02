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

test_get_muncipalities_response_with_paging = {
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
            "name": "Landkreis Kassel",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLandkreis+Kassel&navigation=all",
        },
    ],
    "navigation": [],
    "searchresult": {
        "packages": [],
        "product": {
            "name": "Landkreis Kassel",
            "id": "DC0100066",
            "description": '<b>Digitales Geländemodell (DGM1)</b><br><br>Höhenmäßige Beschreibung des Geländereliefs durch räumliche Repräsentanten in Rasterform (Pixel) mit der quadratischen Fläche von 1 m * 1 m (1 Quadratmeter). Der originäre Höhenbezug ist die Rastermitte. Weitere Informationen zum DGM1 finden Sie <a href="https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle" target="_blank">hier</a>.<ul><i><b>Downloads:</b></i><li><a href="/INTERSHOP/static/WFS/HLBG-Geodaten-Site/-/HLBG-Geodaten/de_DE/Downloadcenter/Daten/3D-Daten/Aktualität_3D_0.pdf" target="_blank">Aktualitätsübersicht DGM1 und DOM1</a></b></i><li><a href="/INTERSHOP/static/WFS/HLBG-Geodaten-Site/-/HLBG-Geodaten/de_DE/Downloadcenter/Daten/3D-Daten/metadatenliste.pdf" target="_blank">metadatenliste</a></li></ul>',
        },
        "downloads": [
            {
                "name": "Ahnatal - DGM1",
                "id": "DP0101060",
                "fileExtension": "ZIP",
                "fileSize": "69,2 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Ahnatal - DGM1.zip",
                },
            },
            {
                "name": "Bad Emstal - DGM1",
                "id": "DP0101061",
                "fileExtension": "ZIP",
                "fileSize": "135,3 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Bad Emstal - DGM1.zip",
                },
            },
            {
                "name": "Bad Karlshafen - DGM1",
                "id": "DP0101062",
                "fileExtension": "ZIP",
                "fileSize": "74,5 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Bad Karlshafen - DGM1.zip",
                },
            },
            {
                "name": "Baunatal - DGM1",
                "id": "DP0101063",
                "fileExtension": "ZIP",
                "fileSize": "134 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Baunatal - DGM1.zip",
                },
            },
            {
                "name": "Breuna - DGM1",
                "id": "DP0101064",
                "fileExtension": "ZIP",
                "fileSize": "134,3 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Breuna - DGM1.zip",
                },
            },
            {
                "name": "Calden - DGM1",
                "id": "DP0101065",
                "fileExtension": "ZIP",
                "fileSize": "169,2 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Calden - DGM1.zip",
                },
            },
            {
                "name": "Espenau - DGM1",
                "id": "DP0101066",
                "fileExtension": "ZIP",
                "fileSize": "51 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Espenau - DGM1.zip",
                },
            },
            {
                "name": "Fuldabrück - DGM1",
                "id": "DP0104851",
                "fileExtension": "ZIP",
                "fileSize": "69,6 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Fuldabrück - DGM1.zip",
                },
            },
            {
                "name": "Fuldatal - DGM1",
                "id": "DP0101068",
                "fileExtension": "ZIP",
                "fileSize": "134,7 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Fuldatal - DGM1.zip",
                },
            },
            {
                "name": "Grebenstein - DGM1",
                "id": "DP0101069",
                "fileExtension": "ZIP",
                "fileSize": "157,3 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Grebenstein - DGM1.zip",
                },
            },
            {
                "name": "Gutsbezirk Reinhardswald - DGM1",
                "id": "DP0101070",
                "fileExtension": "ZIP",
                "fileSize": "606,1 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Gutsbezirk Reinhardswald - DGM1.zip",
                },
            },
            {
                "name": "Habichtswald - DGM1",
                "id": "DP0101071",
                "fileExtension": "ZIP",
                "fileSize": "94,4 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Habichtswald - DGM1.zip",
                },
            },
            {
                "name": "Helsa - DGM1",
                "id": "DP0101072",
                "fileExtension": "ZIP",
                "fileSize": "116,4 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Helsa - DGM1.zip",
                },
            },
            {
                "name": "Hofgeismar - DGM1",
                "id": "DP0101073",
                "fileExtension": "ZIP",
                "fileSize": "274,9 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Hofgeismar - DGM1.zip",
                },
            },
            {
                "name": "Immenhausen - DGM1",
                "id": "DP0101074",
                "fileExtension": "ZIP",
                "fileSize": "97,2 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Immenhausen - DGM1.zip",
                },
            },
            {
                "name": "Kaufungen - DGM1",
                "id": "DP0101075",
                "fileExtension": "ZIP",
                "fileSize": "93,6 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Kaufungen - DGM1.zip",
                },
            },
            {
                "name": "Liebenau - DGM1",
                "id": "DP0101076",
                "fileExtension": "ZIP",
                "fileSize": "165,6 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Liebenau - DGM1.zip",
                },
            },
            {
                "name": "Lohfelden - DGM1",
                "id": "DP0101077",
                "fileExtension": "ZIP",
                "fileSize": "78,2 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Lohfelden - DGM1.zip",
                },
            },
            {
                "name": "Naumburg - DGM1",
                "id": "DP0101078",
                "fileExtension": "ZIP",
                "fileSize": "200,6 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Naumburg - DGM1.zip",
                },
            },
            {
                "name": "Nieste - DGM1",
                "id": "DP0101079",
                "fileExtension": "ZIP",
                "fileSize": "40,6 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Nieste - DGM1.zip",
                },
            },
        ],
        "paging": {
            "total": 29,
            "pageSize": 20,
            "page": 1,
            "url": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLandkreis+Kassel",
        },
    },
}

test_get_muncipalities_response_with_paging_page2 = {
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
            "name": "Landkreis Kassel",
            "uri": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLandkreis+Kassel&navigation=all",
        },
    ],
    "navigation": [],
    "searchresult": {
        "packages": [],
        "product": {
            "name": "Landkreis Kassel",
            "id": "DC0100066",
            "description": '<b>Digitales Geländemodell (DGM1)</b><br><br>Höhenmäßige Beschreibung des Geländereliefs durch räumliche Repräsentanten in Rasterform (Pixel) mit der quadratischen Fläche von 1 m * 1 m (1 Quadratmeter). Der originäre Höhenbezug ist die Rastermitte. Weitere Informationen zum DGM1 finden Sie <a href="https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle" target="_blank">hier</a>.<ul><i><b>Downloads:</b></i><li><a href="/INTERSHOP/static/WFS/HLBG-Geodaten-Site/-/HLBG-Geodaten/de_DE/Downloadcenter/Daten/3D-Daten/Aktualität_3D_0.pdf" target="_blank">Aktualitätsübersicht DGM1 und DOM1</a></b></i><li><a href="/INTERSHOP/static/WFS/HLBG-Geodaten-Site/-/HLBG-Geodaten/de_DE/Downloadcenter/Daten/3D-Daten/metadatenliste.pdf" target="_blank">metadatenliste</a></li></ul>',
        },
        "downloads": [
            {
                "name": "Niestetal - DGM1",
                "id": "DP0101080",
                "fileExtension": "ZIP",
                "fileSize": "82,9 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Niestetal - DGM1.zip",
                },
            },
            {
                "name": "Reinhardshagen - DGM1",
                "id": "DP0101081",
                "fileExtension": "ZIP",
                "fileSize": "81,7 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Reinhardshagen - DGM1.zip",
                },
            },
            {
                "name": "Schauenburg - DGM1",
                "id": "DP0101082",
                "fileExtension": "ZIP",
                "fileSize": "107 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Schauenburg - DGM1.zip",
                },
            },
            {
                "name": "Söhrewald - DGM1",
                "id": "DP0107154",
                "fileExtension": "ZIP",
                "fileSize": "192,7 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Söhrewald - DGM1.zip",
                },
            },
            {
                "name": "Trendelburg - DGM1",
                "id": "DP0101084",
                "fileExtension": "ZIP",
                "fileSize": "235,6 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Trendelburg - DGM1.zip",
                },
            },
            {
                "name": "Vellmar - DGM1",
                "id": "DP0101085",
                "fileExtension": "ZIP",
                "fileSize": "55,3 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Vellmar - DGM1.zip",
                },
            },
            {
                "name": "Wesertal - DGM1",
                "id": "DP0101086",
                "fileExtension": "ZIP",
                "fileSize": "179,6 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Wesertal - DGM1.zip",
                },
            },
            {
                "name": "Wolfhagen - DGM1",
                "id": "DP0101087",
                "fileExtension": "ZIP",
                "fileSize": "333,6 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Wolfhagen - DGM1.zip",
                },
            },
            {
                "name": "Zierenberg - DGM1",
                "id": "DP0101088",
                "fileExtension": "ZIP",
                "fileSize": "258,7 MB",
                "creationDate": "06.05.2024",
                "downloadType": "File",
                "downloadLink": {
                    "name": "Datei herunterladen",
                    "uri": "/downloadcenter/20251102/3D-Daten/Digitales Geländemodell (DGM1)/Landkreis Kassel/Zierenberg - DGM1.zip",
                },
            },
        ],
        "paging": {
            "total": 29,
            "pageSize": 20,
            "page": 2,
            "url": "/INTERSHOP/rest/WFS/HLBG-Geodaten-Site/-/downloadcenter?path=3D-Daten%2FDigitales+Gel%C3%A4ndemodell+%28DGM1%29%2FLandkreis+Kassel",
        },
    },
}
