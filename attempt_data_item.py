import json
import data_item_extractor

data_item = """{
    "entities": {
        "Q4980": {
            "pageid": 211010,
            "ns": 120,
            "title": "Item:Q4980",
            "lastrevid": 2069886,
            "modified": "2020-12-08T20:03:03Z",
            "type": "item",
            "id": "Q4980",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "highway=motorway"
                }
            },
            "descriptions": {
                "en": {
                    "language": "en",
                    "value": "High capacity highways designed to safely carry fast motor traffic."
                },
                "fr": {
                    "language": "fr",
                    "value": "Les motorways sont des routes \u00e0 forte capacit\u00e9 pr\u00e9vues pour faire circuler \u00e0 grande vitesse des v\u00e9hicules motoris\u00e9s, et ce avec un maximum de s\u00e9curit\u00e9."
                }
            },
            "aliases": {},
            "claims": {
                "P2": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2",
                            "hash": "6511c2931be27bcac018d16006b07c7c2e704c57",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 2,
                                    "id": "Q2"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$451AEC5E-9011-4499-B716-31114A205754",
                        "rank": "normal"
                    }
                ],
                "P19": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P19",
                            "hash": "89d6f2061fd696bdef5c77fc1d51a2a220e1c0b8",
                            "datavalue": {
                                "value": "highway=motorway",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "id": "Q4980$207376B7-8A80-453B-B1EC-65D7A30BF7EE",
                        "rank": "normal"
                    }
                ],
                "P10": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P10",
                            "hash": "014a892de5c5de2059647fddb1895987476332dc",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 335,
                                    "id": "Q335"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$EF3DE72C-B170-49F6-980C-A493E1C49E12",
                        "rank": "normal"
                    }
                ],
                "P28": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P28",
                            "hash": "a5f40962e3a489dcf68c2ed590257dd5135b2b39",
                            "datavalue": {
                                "value": "A4-passante di mestre dd.png",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P47": [
                                {
                                    "snaktype": "value",
                                    "property": "P47",
                                    "hash": "f0e21e474aed36c8253a411b2bd64fa7c46663dd",
                                    "datavalue": {
                                        "value": {
                                            "text": "\u0391\u03c5\u03c4\u03bf\u03ba\u03b9\u03bd\u03b7\u03c4\u03cc\u03b4\u03c1\u03bf\u03bc\u03bf\u03c2",
                                            "language": "el"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P47"
                        ],
                        "id": "Q4980$54E94C45-F517-44D3-ABF6-11116E602631",
                        "rank": "preferred"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P28",
                            "hash": "5f0ee64be8af03a097dd16aae0782437d928292f",
                            "datavalue": {
                                "value": "Fi motorway.jpg",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P26": [
                                {
                                    "snaktype": "value",
                                    "property": "P26",
                                    "hash": "87e09586c7e4ca1784661cc50345a6ab6ef200b0",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 7791,
                                            "id": "Q7791"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P26"
                        ],
                        "id": "Q4980$a366600f-4927-9e46-a9fc-c96fbb757e0b",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P28",
                            "hash": "c119b3f8afeec12fd9ac1ff3bba21b5745e1803b",
                            "datavalue": {
                                "value": "LDP-Sunway stretch.JPG",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P26": [
                                {
                                    "snaktype": "value",
                                    "property": "P26",
                                    "hash": "b903c186a8c4aa203ec6fb46660a0d12124d8d2f",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 7803,
                                            "id": "Q7803"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P26"
                        ],
                        "id": "Q4980$BB834ED2-BBCE-436A-A7F3-73629E564B00",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P28",
                            "hash": "fa355505d6b1fbfc30e4f7b3e43c88a4978bd3ea",
                            "datavalue": {
                                "value": "Motorway-DE-A4-Aachen.JPG",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P26": [
                                {
                                    "snaktype": "value",
                                    "property": "P26",
                                    "hash": "e05b66e5c396eb30a261000045022603c63cf8e8",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 6994,
                                            "id": "Q6994"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P26"
                        ],
                        "id": "Q4980$AC454E1D-7BC2-4C44-92DF-D549165DABC9",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P28",
                            "hash": "09d2a4e79db7720c5e581c006d1553d8deabf634",
                            "datavalue": {
                                "value": "Motorway-photo.jpg",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P26": [
                                {
                                    "snaktype": "value",
                                    "property": "P26",
                                    "hash": "b80d4a1cce96cb7e00486d116b9b599db45ec1e4",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 7804,
                                            "id": "Q7804"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P26",
                                    "hash": "30c8a50eb212251f44fe7652c8a3cb6cda4ac04d",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 7792,
                                            "id": "Q7792"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P26",
                                    "hash": "4fce53cd2f2789c33faa8a09ac7ff8e28ebc4dce",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 7798,
                                            "id": "Q7798"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P26",
                                    "hash": "8a06ee7969c5eee29022df9642c0c1fa0b165d22",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 7809,
                                            "id": "Q7809"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P26"
                        ],
                        "id": "Q4980$7F94F4BE-B458-491F-A599-FBF672259936",
                        "rank": "normal"
                    }
                ],
                "P39": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P39",
                            "hash": "8c2710f51d353ee059449687d83b7dd410db4eb7",
                            "datavalue": {
                                "value": "Rendering-highway motorway carto.png",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "id": "Q4980$31A71B40-4431-4F1C-8762-2C6E8BE37BDD",
                        "rank": "preferred"
                    }
                ],
                "P6": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P6",
                            "hash": "437d526f9bb548f06af052a3bb0f3e71a63f0e42",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 13,
                                    "id": "Q13"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$07768FBE-1C69-4B24-9718-20BFF5AD9D26",
                        "rank": "preferred"
                    }
                ],
                "P33": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P33",
                            "hash": "d05308c00623db4b62dc663bc78b43e1414ef85a",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 8001,
                                    "id": "Q8001"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$C37A3714-D794-442A-AE82-5ED5560DB000",
                        "rank": "preferred"
                    }
                ],
                "P34": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P34",
                            "hash": "0020131857e3f842017ae00fb42c27556e40ba4d",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 8000,
                                    "id": "Q8000"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$8F430C53-BF26-4675-9D66-2A5B39A34EF5",
                        "rank": "preferred"
                    }
                ],
                "P35": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P35",
                            "hash": "55f48edfdf46fe5545fc46f1710c58b9361cba0f",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 8001,
                                    "id": "Q8001"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$8A4B3DDA-03C6-4414-A495-C8DE51C7E8C8",
                        "rank": "preferred"
                    }
                ],
                "P36": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P36",
                            "hash": "da59fea04a91ec684c883ff2db27de2c13a3875e",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 8001,
                                    "id": "Q8001"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$F746D945-225C-4927-87F1-26B87EF63D73",
                        "rank": "preferred"
                    }
                ],
                "P25": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P25",
                            "hash": "0bd166bd246e1a8ac5e24f887b893848fc76a421",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 4673,
                                    "id": "Q4673"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$B29E67C6-CE81-4D84-A7D5-873ADA1925D6",
                        "rank": "preferred"
                    }
                ],
                "P12": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P12",
                            "hash": "142ff235d19e27cff6f0782584ce166ccd4ec659",
                            "datavalue": {
                                "value": "Q46622",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q4980$81F89785-176E-4DD0-ACFD-56F48086E566",
                        "rank": "preferred"
                    }
                ],
                "P45": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P45",
                            "hash": "bac29fc5820621891958078576b1409089c5c954",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 16174,
                                    "id": "Q16174"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$E78F2C6C-6B6F-4922-A122-CFC7952DFDE9",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P45",
                            "hash": "3af83650f40eedcc3f3c64d78bbb6141ce039f5e",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 19421,
                                    "id": "Q19421"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$51A5F14B-C648-4F68-B8F1-808D37D63F9D",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P45",
                            "hash": "bd799db7a36b5b622b01c195093e5ea0c987c4d3",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 19518,
                                    "id": "Q19518"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$B6430C4E-2CE9-4885-81C5-9510AB5B7595",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P45",
                            "hash": "4d090b619ce3fd3f47cbb8c69d87a215a770ae3f",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 19521,
                                    "id": "Q19521"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$94840D9B-8B17-4C01-AFB3-95C22EA3A854",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P45",
                            "hash": "bd96f6230dc6c281ed0d79f0be78f3fc44aa3be4",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 19522,
                                    "id": "Q19522"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$627E6E0C-13F2-4AA4-B044-3CE22C78CA46",
                        "rank": "normal"
                    }
                ],
                "P46": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "38f693da914702116d727131a8914f26686214ed",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 219,
                                    "id": "Q219"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$06CAF0FA-757B-4FB7-B59A-8EB01F18FC8F",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "c1d869c526259e060ec99b4f9aa258f92f3f2fa2",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 372,
                                    "id": "Q372"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$2565F219-8D22-4776-8839-9D4F7CAB3434",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "b97d4332a0de3c31dbd4677c02d09261c8ae121c",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 464,
                                    "id": "Q464"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$5008349E-553A-4FF1-AFA3-E12EC536814E",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "57fed57ffaa954aba7f0175a775c7184d2805318",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 599,
                                    "id": "Q599"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$23017979-5310-4617-987B-A2DE5CD4D4CB",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "b26762b43d8101b26477f4e5c0c8732230464853",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 775,
                                    "id": "Q775"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$002EEC9A-AD4A-4A96-B2BA-0232FFB5D626",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "edfc3f39b51b5b4e3b988d26029e8dca55320db0",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 19421,
                                    "id": "Q19421"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4980$EA1733BB-337D-47A9-8D41-18900EDB750C",
                        "rank": "normal"
                    }
                ],
                "P31": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "dab687436981d95d31560ec71ee09adf664dbd4c",
                            "datavalue": {
                                "value": {
                                    "text": "Tag:highway=motorway",
                                    "language": "en"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$2846C321-CABA-4BB7-A16E-E242EF39F0CF",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "ab9ea325eb00d388ec7e8765a6ba9d152f3232ae",
                            "datavalue": {
                                "value": {
                                    "text": "Cs:Tag:highway=motorway",
                                    "language": "cs"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$7BBCA3F3-D205-40A2-A191-532B257B0984",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "00450dd977b35b9cd1109e4dbb7c94e2cd4ed427",
                            "datavalue": {
                                "value": {
                                    "text": "DE:Tag:highway=motorway",
                                    "language": "de"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$94EA01ED-9828-4742-91DF-F5627F0B7100",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "d31bee276b32e993997742c545497f6b0a4cb352",
                            "datavalue": {
                                "value": {
                                    "text": "El:Tag:highway=motorway",
                                    "language": "el"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$2481E952-31CF-4763-B37B-240BC2DF68A3",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "62a5509335ae36ef6d0da31b2a0f3671ce3761fb",
                            "datavalue": {
                                "value": {
                                    "text": "ES:Tag:highway=motorway",
                                    "language": "es"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$98DDE0D0-8BE8-4B49-B15F-536BC06604CA",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "79287b0fd34c29679902911116aca70546de3626",
                            "datavalue": {
                                "value": {
                                    "text": "FR:Tag:highway=motorway",
                                    "language": "fr"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$4163659D-19F8-44DD-A1B8-F1D6D3177EC6",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "f60dd95f621f90d4d5aff609643783ba80fecee9",
                            "datavalue": {
                                "value": {
                                    "text": "IT:Tag:highway=motorway",
                                    "language": "it"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$5D0FF3F5-A31B-457A-B212-7AFC58CFA386",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "24e2df09f0ff4bd995c966c2e6e07b9672993796",
                            "datavalue": {
                                "value": {
                                    "text": "JA:Tag:highway=motorway",
                                    "language": "ja"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$AA8CB350-D47C-4160-8E15-3A24064BAEAF",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "e67c06ac1f39c5eb258bbc7c86fad72aa4257c86",
                            "datavalue": {
                                "value": {
                                    "text": "Ko:Tag:highway=motorway",
                                    "language": "ko"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$87B4EBD1-DC5C-4047-A0AC-63F4AB5CE917",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "3da78157ef1ee099f9fdb6ec19f6e220b2ae1fd0",
                            "datavalue": {
                                "value": {
                                    "text": "Ms:Tag:highway=motorway",
                                    "language": "ms"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$E14B2D48-102D-409A-B2A0-DAE04326B7C5",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "0b5671709f70c16801fe12dbbfaa4e1c5959716d",
                            "datavalue": {
                                "value": {
                                    "text": "NL:Tag:highway=motorway",
                                    "language": "nl"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$BEFA150A-FF77-49E5-8EDD-3ECA3E3A73FE",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "6cb860af6e7f39bd173b10eae2c3cca56828786a",
                            "datavalue": {
                                "value": {
                                    "text": "Pl:Tag:highway=motorway",
                                    "language": "pl"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$1AFE9ED6-D502-4F5F-8DED-BC8692F50B53",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "8abc96313b94cf634bb8c9a51d0668aa7531c401",
                            "datavalue": {
                                "value": {
                                    "text": "Pt:Tag:highway=motorway",
                                    "language": "pt"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$781DC2C8-7140-40CB-AF3B-892A293B699F",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "b14370a386f99ce95ff20c47584aeadde3f0be01",
                            "datavalue": {
                                "value": {
                                    "text": "Pt-br:Tag:highway=motorway",
                                    "language": "pt-br"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P50": [
                                {
                                    "snaktype": "value",
                                    "property": "P50",
                                    "hash": "a534bfe55e56ac09ed343d89fa88d8b57f71d0bc",
                                    "datavalue": {
                                        "value": "Pt:Tag:highway=motorway",
                                        "type": "string"
                                    },
                                    "datatype": "string"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P50"
                        ],
                        "id": "Q4980$796A4E61-A61D-4A74-9BE3-5BD71CAC289C",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "42e6e4fabfdeb60f86f722dfacd4171e0ca47fd7",
                            "datavalue": {
                                "value": {
                                    "text": "RU:Tag:highway=motorway",
                                    "language": "ru"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$1F5CB1E7-15A4-4BD4-AC04-15BE1CC4F95C",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "a9600872d57934b4850eed87c235d2647898ca3a",
                            "datavalue": {
                                "value": {
                                    "text": "Tr:Tag:highway=motorway",
                                    "language": "tr"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$2A9E7F1A-1C66-4997-AF81-7245927D229F",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "060b5ad15624394daf469fbc06e5616f80f8cca1",
                            "datavalue": {
                                "value": {
                                    "text": "Uk:Tag:highway=motorway",
                                    "language": "uk"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$5C9411B6-42C0-4358-B08D-C7D2B4EC9B09",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "26167417bf49bd67177b13abd030fefbb16a496f",
                            "datavalue": {
                                "value": {
                                    "text": "Zh-hant:Tag:highway=motorway",
                                    "language": "zh-hant"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4980$E81B6A52-2326-40A6-9101-E5BF8A8FC126",
                        "rank": "normal"
                    }
                ]
            },
            "sitelinks": {
                "wiki": {
                    "site": "wiki",
                    "title": "Tag:highway=motorway",
                    "badges": []
                }
            }
        }
    },
    "success": 1
}"""


parsed = json.loads(data_item)

returned = data_item_extractor.turn_api_response_to_parsed(parsed)
print(returned)