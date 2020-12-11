# Copyright (C) 2020  Mateusz Konieczny <matkoniecz@gmail.com>
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License 3 as published by FSF

import json
import extract_data_item

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

university_text = """
{
    "entities": {
        "Q4736": {
            "pageid": 210765,
            "ns": 120,
            "title": "Item:Q4736",
            "lastrevid": 2052768,
            "modified": "2020-10-22T20:35:49Z",
            "type": "item",
            "id": "Q4736",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "amenity=university"
                }
            },
            "descriptions": {
                "en": {
                    "language": "en",
                    "value": "An educational institution designed for instruction, examination, or both, of students in many branches of advanced learning."
                },
                "fr": {
                    "language": "fr",
                    "value": "Un \u00e9tablissement d\u2019enseignement universitaire."
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
                        "id": "Q4736$66FC33F7-1CA5-4072-ABBE-490AF2054C69",
                        "rank": "normal"
                    }
                ],
                "P19": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P19",
                            "hash": "cb061476e539eada26f0e5e403856bce14780343",
                            "datavalue": {
                                "value": "amenity=university",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "id": "Q4736$82E5F3D0-12F8-4D63-AD21-752B8A58342B",
                        "rank": "normal"
                    }
                ],
                "P10": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P10",
                            "hash": "1328a252ed5de0baf77d66a1640301b6dfe18308",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 61,
                                    "id": "Q61"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4736$59F81DE4-DE7E-4514-9D96-767CC2BC59C1",
                        "rank": "normal"
                    }
                ],
                "P28": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P28",
                            "hash": "255ddd779cecf1b346823eef31b9433e301a7d59",
                            "datavalue": {
                                "value": "Dscf1076 600.jpg",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "id": "Q4736$5CECD7D6-E139-4E64-A42A-5ECB51EB35B6",
                        "rank": "preferred"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P28",
                            "hash": "7509218b3d7e028545fb1bd1be863daaf9679e5e",
                            "datavalue": {
                                "value": "Uniwersytet Jagiello\u0144ski, Collegium Novum.JPG",
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
                                    "hash": "d467e092d2f9541bac5a796ddf95a2101b3f619e",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 7806,
                                            "id": "Q7806"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ],
                            "P47": [
                                {
                                    "snaktype": "value",
                                    "property": "P47",
                                    "hash": "c88607de9ada8af5d70f765405a9f4514810abd2",
                                    "datavalue": {
                                        "value": {
                                            "text": "Uniwersytet Jagiello\u0144ski, Collegium Novum.",
                                            "language": "pl"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P26",
                            "P47"
                        ],
                        "id": "Q4736$F952BE05-3E0E-4DA5-9EF4-1195CC0721F6",
                        "rank": "normal"
                    }
                ],
                "P39": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P39",
                            "hash": "eb0f8c5170b0f9b2fbbfd6508d339372d36fd078",
                            "datavalue": {
                                "value": "Rendering-area-amenity-school.png",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "id": "Q4736$92F4A8C8-E609-4B99-AE6D-BAF0B7F41E58",
                        "rank": "preferred"
                    }
                ],
                "P6": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P6",
                            "hash": "b2c07cc9f42392a0a80595b5b6c968e50068ffa0",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 15,
                                    "id": "Q15"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4736$171D1C07-BE40-45E1-B4FF-C4F4E9D0D95C",
                        "rank": "preferred"
                    }
                ],
                "P33": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P33",
                            "hash": "787ef76c487fb28eedcc10c388fb4245e2b92e0f",
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
                        "id": "Q4736$09E675D1-C0C6-4334-B170-0D22499414B3",
                        "rank": "preferred"
                    }
                ],
                "P34": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P34",
                            "hash": "9b6067afea85541b88f2bac304657bd2e8962e0d",
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
                        "id": "Q4736$5144C882-3FA8-4138-B8A5-5B92E168EF90",
                        "rank": "preferred"
                    }
                ],
                "P35": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P35",
                            "hash": "8d54b8f7391e3f783fe3d76d15d9036b90305842",
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
                        "id": "Q4736$BEA7AFA9-A5D8-4E5D-830F-225F2E295572",
                        "rank": "preferred"
                    }
                ],
                "P36": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P36",
                            "hash": "724c9a8f85dfb6c9de78ecb25a7504e02b40a8c7",
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
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P26",
                                    "hash": "f9e806c2f33e02433219e0d7672f15f5ac62b020",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 7788,
                                            "id": "Q7788"
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
                        "id": "Q4736$7D653833-16E5-40F6-A91E-005DC27E07C9",
                        "rank": "normal"
                    },
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
                        "qualifiers": {
                            "P26": [
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
                        "id": "Q4736$50E22041-4577-4458-A112-6E19290D2773",
                        "rank": "normal"
                    }
                ],
                "P12": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P12",
                            "hash": "2499807cbd6ad8f165de1cf91b5cc42ff1b569dc",
                            "datavalue": {
                                "value": "Q3918",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q4736$190131C1-0524-4EF7-89B3-3A3F351AB6D8",
                        "rank": "preferred"
                    }
                ],
                "P46": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "3335bd20921b46c31e02654c618c04fc8b0eca72",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 174,
                                    "id": "Q174"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4736$B89B3FBB-AF9B-4428-B39A-ECF57546BCA8",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "d4cad755ff16c779f89cc7ab671537ac5fbec91a",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 35,
                                    "id": "Q35"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4736$80EB667D-1563-4E9D-99B7-5CA988658113",
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
                        "id": "Q4736$133517BB-E894-4078-8F5B-B1FACB25D5A8",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "f21c4383bc67c702ae0572cca35e91c9e5e94ce2",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 524,
                                    "id": "Q524"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4736$2352FAA6-70C8-43B5-B1F4-7A9DA3B277FF",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P46",
                            "hash": "3077616b4115dcc33718e9e18b75aef6240446b7",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 828,
                                    "id": "Q828"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q4736$DCB9BC6A-4581-4A29-8852-FEF6656F4690",
                        "rank": "normal"
                    }
                ],
                "P31": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "fff664f19e8e37b88ef79acbad71ea04dc200574",
                            "datavalue": {
                                "value": {
                                    "text": "Tag:amenity=university",
                                    "language": "en"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$996B8338-7EEE-4B93-B3C5-716B09B42A91",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "08d79d7aaebb70a97aeb62ee803d7f74992c713b",
                            "datavalue": {
                                "value": {
                                    "text": "Cs:Tag:amenity=university",
                                    "language": "cs"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$F0E68AD9-EC11-488F-B29C-F1D3B080B7EE",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "121d8564834545bf361b04652564a4e22c1777d7",
                            "datavalue": {
                                "value": {
                                    "text": "DE:Tag:amenity=university",
                                    "language": "de"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$5068C6E6-CE2D-46DD-9ADA-DF6231E07F35",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "f0f8c09008838af996c4e77a43535506322b9f6e",
                            "datavalue": {
                                "value": {
                                    "text": "El:Tag:amenity=university",
                                    "language": "el"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$480C0D57-31D3-4719-B603-760320A83A22",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "398e477e8a6a969338efbbf87ab3a48f8bd900f4",
                            "datavalue": {
                                "value": {
                                    "text": "ES:Tag:amenity=university",
                                    "language": "es"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$3C6A86FA-F5F7-44F9-BEE5-A11F70DDABA1",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "ca0d7a9d21102b0fc09631a89c3c06eb562ed05c",
                            "datavalue": {
                                "value": {
                                    "text": "FR:Tag:amenity=university",
                                    "language": "fr"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$E0645E70-7F7B-4191-8455-E3B3282ACC80",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "fd1dd8eca569710786cee36032cf8ec92c405641",
                            "datavalue": {
                                "value": {
                                    "text": "IT:Tag:amenity=university",
                                    "language": "it"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$C48BAAEC-85EC-44AB-8091-E73E945B65F2",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "1012d88cf75857dc88383cf4c37a15f2ffcb0c57",
                            "datavalue": {
                                "value": {
                                    "text": "JA:Tag:amenity=university",
                                    "language": "ja"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$26ED17F5-A65E-4980-B861-0B97F452BEDC",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "8a57f13405765811ce82957332e4acd2031f0ff5",
                            "datavalue": {
                                "value": {
                                    "text": "Pl:Tag:amenity=university",
                                    "language": "pl"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$A03C58C8-3EB6-4068-918F-AFF7F03BFA1C",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "af997b9d513df1e25a286d1293e3171ab0467e96",
                            "datavalue": {
                                "value": {
                                    "text": "Pt:Tag:amenity=university",
                                    "language": "pt"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$9D5DAD63-6272-4113-8BE6-66C89B6C1609",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "aa9c62d74453fe79dd2be2374c778cea5a23480c",
                            "datavalue": {
                                "value": {
                                    "text": "Pt-br:Tag:amenity=university",
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
                                    "hash": "28956fc1b7060e8faeb6bc18885e718d29ca2a94",
                                    "datavalue": {
                                        "value": "Pt:Tag:amenity=university",
                                        "type": "string"
                                    },
                                    "datatype": "string"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P50"
                        ],
                        "id": "Q4736$E4E7279C-F5A0-45E8-85AD-ED7CCEB13D43",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "1db1e426fd55d31530c085a1bcc3095466312659",
                            "datavalue": {
                                "value": {
                                    "text": "RU:Tag:amenity=university",
                                    "language": "ru"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$BFBCA8F4-67EA-4AB3-A708-B31919D24AA8",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "2ae1e8faf7c2f9cc53556dfcc57bacb29851fc3b",
                            "datavalue": {
                                "value": {
                                    "text": "Uk:Tag:amenity=university",
                                    "language": "uk"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q4736$EF847B1F-18D0-4A15-8C24-F0D021DD3DDE",
                        "rank": "normal"
                    }
                ]
            },
            "sitelinks": {
                "wiki": {
                    "site": "wiki",
                    "title": "Tag:amenity=university",
                    "badges": []
                }
            }
        }
    },
    "success": 1
}
"""

parsed = json.loads(data_item)
returned = extract_data_item.turn_api_response_to_parsed(parsed)
print(returned)

parsed = json.loads(university_text)
returned = extract_data_item.turn_api_response_to_parsed(parsed)
print(returned)