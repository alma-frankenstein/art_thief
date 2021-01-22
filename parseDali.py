#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# change 'true', 'false' and 'null' to 'True', 'False' and 'None'

import json

dali = [
  [
    {
      "queryID": "artworkRoutes_ArtworkQuery",
      "variables": {
        "artworkID": "salvador-dali-madonne"
      }
    },
    {
      "ok": True,
      "status": 200,
      "url": "https://metaphysics-production.artsy.net/v2",
      "headers": {
        "_headers": {
          "server": [
            "nginx/1.17.10"
          ],
          "date": [
            "Wed, 20 Jan 2021 19:45:33 GMT"
          ],
          "content-type": [
            "application/json; charset=utf-8"
          ],
          "transfer-encoding": [
            "chunked"
          ],
          "connection": [
            "close"
          ],
          "x-powered-by": [
            "Express"
          ],
          "access-control-allow-origin": [
            "*"
          ],
          "etag": [
            "W/\"dab2-A5Y1WcCNFiNWL7ESCe8nk5VaaQ8\""
          ],
          "vary": [
            "Accept-Encoding"
          ],
          "content-encoding": [
            "gzip"
          ],
          "strict-transport-security": [
            "max-age=15724800; includeSubDomains"
          ]
        }
      },
      "json": {
        "data": {
          "artwork": {
            "slug": "salvador-dali-madonne",
            "internalID": "5dc6a4d496c491000e5bb170",
            "is_acquireable": False,
            "is_offerable": False,
            "availability": "for sale",
            "listPrice": {
              "__typename": "PriceRange",
              "display": "€5,000 - 7,500",
              "minPrice": {
                "major": 5000,
                "currencyCode": "EUR",
                "minor": 500000
              },
              "maxPrice": {
                "major": 7500,
                "minor": 750000
              }
            },
            "is_in_auction": False,
            "sale": None,
            "artists": [
              {
                "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                "slug": "salvador-dali",
                "internalID": "4dadcce67129f059240009df",
                "name": "Salvador Dalí",
                "href": "/artist/salvador-dali",
                "image": {
                  "cropped": {
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=100&height=100&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FD8nvgg6qr0fmPkx9fzzj-Q%2Flarge.jpg"
                  }
                },
                "formatted_nationality_and_birthday": "Spanish, 1904–1989",
                "counts": {
                  "partner_shows": 143,
                  "follows": 31759
                },
                "exhibition_highlights": [
                  {
                    "partner": {
                      "__typename": "Partner",
                      "name": "Opera Gallery",
                      "id": "UGFydG5lcjo1MGQxYTcyYjEyNzIzMDgxOTcwMDA0NDU="
                    },
                    "name": "Masterpiece Collection / Singapore",
                    "start_at": "2019",
                    "cover_image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FU9DrqRPAqDnAyaHkdmPTPQ%2Flarge.jpg"
                      }
                    },
                    "city": "Singapore",
                    "id": "U2hvdzo1ZDY3ZDdiODc4ZWVlNzAwMTM0ZjY0OGQ="
                  },
                  {
                    "partner": {
                      "__typename": "Partner",
                      "name": "Opera Gallery",
                      "id": "UGFydG5lcjo1MGQxYTcyYjEyNzIzMDgxOTcwMDA0NDU="
                    },
                    "name": "Salvador Dalí",
                    "start_at": "2015",
                    "cover_image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FVspDps0UOe3b85_H7mSexw%2Flarge.jpg"
                      }
                    },
                    "city": "Singapore",
                    "id": "U2hvdzo1NWRmMjUwZTcyNjE2OTNkOWIwMDAwZTg="
                  },
                  {
                    "partner": {
                      "__typename": "Partner",
                      "name": "Kunstmuseum Bern",
                      "id": "UGFydG5lcjo1NTEzMTlhMTcyNjE2OTFmZDAwZjA5MDA="
                    },
                    "name": "Highlights from Kunstmuseum Bern",
                    "start_at": "2016",
                    "cover_image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FNMq6w3co7aUecadVsUZnLw%2Flarge.jpg"
                      }
                    },
                    "city": "Bern",
                    "id": "U2hvdzo1NzFlODY1OGNkNTMwZTY1OTcwMDA4ODQ="
                  }
                ],
                "collections": [
                  "Tate",
                  "Museum of Modern Art (MoMA)",
                  "Indianapolis Museum of Art at Newfields",
                  "de la Cruz Collection"
                ],
                "highlights": {
                  "partnersConnection": {
                    "edges": []
                  }
                },
                "auctionResultsConnection": {
                  "edges": [
                    {
                      "node": {
                        "__typename": "AuctionResult",
                        "id": "QXVjdGlvblJlc3VsdDozMjQ0NDI5",
                        "price_realized": {
                          "display": "£13m"
                        },
                        "organization": "Sotheby's",
                        "sale_date": "2011"
                      }
                    }
                  ]
                },
                "biographyBlurb": {
                  "text": "<p>Salvador Dalí was a leading proponent of <a href=\"/gene/surrealism\">Surrealism<\/a>, the 20-century avant-garde movement that sought to release the creative potential of the unconscious through strange, dream-like imagery. “<a href=\"/gene/surrealism\">Surrealism<\/a> is destructive, but it destroys only what it considers to be shackles limiting our vision,” he said. Dalí is specially credited with the innovation of “paranoia-criticism,” a philosophy of art making he defined as “irrational understanding based on the interpretive-critical association of delirious phenomena.” In addition to meticulously painting fantastic compositions, such as <em>The Accommodations of Desire<\/em> (1929) and the <a href=\"/collection/salvador-dali-melting-clocks\">melting clocks<\/a> in his famed <em>The Persistence of Memory<\/em> (1931), Dalí was a prolific writer and early filmmaker, and cultivated an eccentric public persona with his flamboyant mustache, pet ocelot, and outlandish behavior and quips. <\/p>\n"
                },
                "is_followed": False,
                "related": {
                  "suggestedConnection": None
                },
                "is_consignable": True
              }
            ],
            "artist": {
              "internalID": "4dadcce67129f059240009df",
              "slug": "salvador-dali",
              "name": "Salvador Dalí",
              "href": "/artist/salvador-dali",
              "image": {
                "cropped": {
                  "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=100&height=100&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FD8nvgg6qr0fmPkx9fzzj-Q%2Flarge.jpg"
                }
              },
              "formatted_nationality_and_birthday": "Spanish, 1904–1989",
              "counts": {
                "partner_shows": 143,
                "follows": 31759
              },
              "exhibition_highlights": [
                {
                  "partner": {
                    "__typename": "Partner",
                    "name": "Opera Gallery",
                    "id": "UGFydG5lcjo1MGQxYTcyYjEyNzIzMDgxOTcwMDA0NDU="
                  },
                  "name": "Masterpiece Collection / Singapore",
                  "start_at": "2019",
                  "cover_image": {
                    "cropped": {
                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FU9DrqRPAqDnAyaHkdmPTPQ%2Flarge.jpg"
                    }
                  },
                  "city": "Singapore",
                  "id": "U2hvdzo1ZDY3ZDdiODc4ZWVlNzAwMTM0ZjY0OGQ="
                },
                {
                  "partner": {
                    "__typename": "Partner",
                    "name": "Opera Gallery",
                    "id": "UGFydG5lcjo1MGQxYTcyYjEyNzIzMDgxOTcwMDA0NDU="
                  },
                  "name": "Salvador Dalí",
                  "start_at": "2015",
                  "cover_image": {
                    "cropped": {
                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FVspDps0UOe3b85_H7mSexw%2Flarge.jpg"
                    }
                  },
                  "city": "Singapore",
                  "id": "U2hvdzo1NWRmMjUwZTcyNjE2OTNkOWIwMDAwZTg="
                },
                {
                  "partner": {
                    "__typename": "Partner",
                    "name": "Kunstmuseum Bern",
                    "id": "UGFydG5lcjo1NTEzMTlhMTcyNjE2OTFmZDAwZjA5MDA="
                  },
                  "name": "Highlights from Kunstmuseum Bern",
                  "start_at": "2016",
                  "cover_image": {
                    "cropped": {
                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FNMq6w3co7aUecadVsUZnLw%2Flarge.jpg"
                    }
                  },
                  "city": "Bern",
                  "id": "U2hvdzo1NzFlODY1OGNkNTMwZTY1OTcwMDA4ODQ="
                }
              ],
              "collections": [
                "Tate",
                "Museum of Modern Art (MoMA)",
                "Indianapolis Museum of Art at Newfields",
                "de la Cruz Collection"
              ],
              "highlights": {
                "partnersConnection": {
                  "edges": []
                }
              },
              "auctionResultsConnection": {
                "edges": [
                  {
                    "node": {
                      "__typename": "AuctionResult",
                      "id": "QXVjdGlvblJlc3VsdDozMjQ0NDI5",
                      "price_realized": {
                        "display": "£13m"
                      },
                      "organization": "Sotheby's",
                      "sale_date": "2011"
                    }
                  }
                ]
              },
              "biographyBlurb": {
                "text": "<p>Salvador Dalí was a leading proponent of <a href=\"/gene/surrealism\">Surrealism<\/a>, the 20-century avant-garde movement that sought to release the creative potential of the unconscious through strange, dream-like imagery. “<a href=\"/gene/surrealism\">Surrealism<\/a> is destructive, but it destroys only what it considers to be shackles limiting our vision,” he said. Dalí is specially credited with the innovation of “paranoia-criticism,” a philosophy of art making he defined as “irrational understanding based on the interpretive-critical association of delirious phenomena.” In addition to meticulously painting fantastic compositions, such as <em>The Accommodations of Desire<\/em> (1929) and the <a href=\"/collection/salvador-dali-melting-clocks\">melting clocks<\/a> in his famed <em>The Persistence of Memory<\/em> (1931), Dalí was a prolific writer and early filmmaker, and cultivated an eccentric public persona with his flamboyant mustache, pet ocelot, and outlandish behavior and quips. <\/p>\n"
              },
              "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
              "is_followed": False,
              "related": {
                "artistsConnection": {
                  "pageInfo": {
                    "hasNextPage": True,
                    "endCursor": "YXJyYXljb25uZWN0aW9uOjM="
                  },
                  "edges": [
                    {
                      "node": {
                        "name": "Max Ernst",
                        "slug": "max-ernst",
                        "href": "/artist/max-ernst",
                        "image": {
                          "cropped": {
                            "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FUUEzIl7siZqz25gXGIFAbA%2Flarge.jpg"
                          }
                        },
                        "formatted_nationality_and_birthday": "German, 1891–1976",
                        "id": "QXJ0aXN0OjRkZTZiNGRlYTllNjg3MDAwMTAwMDc1Zg==",
                        "internalID": "4de6b4dea9e687000100075f",
                        "is_followed": False,
                        "counts": {
                          "follows": 9595
                        },
                        "__typename": "Artist"
                      },
                      "cursor": "YXJyYXljb25uZWN0aW9uOjA="
                    },
                    {
                      "node": {
                        "name": "René Magritte",
                        "slug": "rene-magritte",
                        "href": "/artist/rene-magritte",
                        "image": {
                          "cropped": {
                            "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FS4YIgw6IeYJjMFuCLJoAVg%2Flarge.jpg"
                          }
                        },
                        "formatted_nationality_and_birthday": "Belgian, 1898–1967",
                        "id": "QXJ0aXN0OjRlOTc0YmFlMDMwNzgwMDAwMTAwMTk2Ng==",
                        "internalID": "4e974bae0307800001001966",
                        "is_followed": False,
                        "counts": {
                          "follows": 13235
                        },
                        "__typename": "Artist"
                      },
                      "cursor": "YXJyYXljb25uZWN0aW9uOjE="
                    },
                    {
                      "node": {
                        "name": "Joan Miró",
                        "slug": "joan-miro",
                        "href": "/artist/joan-miro",
                        "image": {
                          "cropped": {
                            "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FDvZH9-qtZotZ5w1596tctA%2Flarge.jpg"
                          }
                        },
                        "formatted_nationality_and_birthday": "Spanish, 1893–1983",
                        "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                        "internalID": "4d8b927f4eb68a1b2c00017c",
                        "is_followed": False,
                        "counts": {
                          "follows": 22266
                        },
                        "__typename": "Artist"
                      },
                      "cursor": "YXJyYXljb25uZWN0aW9uOjI="
                    },
                    {
                      "node": {
                        "name": "Eugene Berman",
                        "slug": "eugene-berman",
                        "href": "/artist/eugene-berman",
                        "image": {
                          "cropped": {
                            "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FjG2rr_ZOZczN0UuAhANQPQ%2Flarge.jpg"
                          }
                        },
                        "formatted_nationality_and_birthday": "American, 1899–1972",
                        "id": "QXJ0aXN0OjUyOGU3NDRiMWExZTg2ZDQ4YzAwMDA4ZA==",
                        "internalID": "528e744b1a1e86d48c00008d",
                        "is_followed": False,
                        "counts": {
                          "follows": 338
                        },
                        "__typename": "Artist"
                      },
                      "cursor": "YXJyYXljb25uZWN0aW9uOjM="
                    }
                  ]
                }
              }
            },
            "href": "/artwork/salvador-dali-madonne",
            "date": "1957",
            "artist_names": "Salvador Dalí",
            "sale_message": "€5,000 - 7,500",
            "partner": {
              "name": "Dali Paris",
              "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
              "type": "Gallery",
              "profile": {
                "image": {
                  "resized": {
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FpJInfgBNj3NB4QK1x_0HHQ%2Fmedium250x165.jpg"
                  }
                },
                "id": "UHJvZmlsZTo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzI=",
                "slug": "dali-paris",
                "name": "Dali Paris",
                "internalID": "592ea16eb202a34d9949b732",
                "is_followed": False,
                "icon": {
                  "url": "https://d32dm0rphc51dk.cloudfront.net/XOf_yFqYK5o4fj3iDVqWOA/square140.png"
                }
              },
              "initials": "DP",
              "href": "/dali-paris",
              "locations": [
                {
                  "city": "Paris",
                  "id": "TG9jYXRpb246NTkyZWEzY2Y4YjNiODE2OTkwZTA5ZjY5"
                }
              ],
              "isVerifiedSeller": False,
              "internalID": "592ea16eb202a34d9949b731",
              "slug": "dali-paris",
              "is_default_profile_public": True
            },
            "image_rights": "",
            "is_shareable": True,
            "meta_image": {
              "resized": {
                "width": 640,
                "height": 1031,
                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=640&height=1031&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FdAMtqpwtIUgN0zlJpjYrmA%2Flarge.jpg"
              }
            },
            "meta": {
              "title": "Salvador Dalí | Madonne (1957) | Available for Sale | Artsy",
              "description": "Available for sale from Dali Paris, Salvador Dalí, Madonne (1957), Lithograph, 64.5 × 41 cm",
              "long_description": "Available for sale from Dali Paris, Salvador Dalí, Madonne (1957), Lithograph, 64.5 × 41 cm"
            },
            "context": None,
            "is_price_hidden": False,
            "is_price_range": True,
            "category": "Drawing, Collage or other Work on Paper",
            "dimensions": {
              "in": "25 2/5 × 16 1/10 in",
              "cm": "64.5 × 41 cm"
            },
            "cultural_maker": None,
            "is_biddable": False,
            "edition_sets": [
              {
                "__typename": "EditionSet",
                "id": "RWRpdGlvblNldDo1ZmM0YWMyOGJhNTQxYTNmMjliOWI4YmE=",
                "internalID": "5fc4ac28ba541a3f29b9b8ba",
                "is_acquireable": False,
                "is_offerable": False,
                "sale_message": "€5,000 - 7,500",
                "dimensions": {
                  "in": "25 2/5 × 16 1/10 in",
                  "cm": "64.5 × 41 cm"
                },
                "edition_of": "Edition of 233"
              }
            ],
            "sale_artwork": None,
            "title": "Madonne",
            "medium": "Lithograph",
            "edition_of": "Edition of 233",
            "attributionClass": {
              "shortDescription": "This work is part of a limited edition set",
              "id": "QXR0cmlidXRpb25DbGFzczpsaW1pdGVkIGVkaXRpb24="
            },
            "myLotStanding": None,
            "is_for_sale": True,
            "is_inquireable": True,
            "priceIncludesTaxDisplay": "VAT included in price",
            "shippingInfo": "Shipping: €150 within Continental Europe, €250 rest of world",
            "shippingOrigin": "Paris, FR",
            "hasCertificateOfAuthenticity": True,
            "description": None,
            "additional_information": "<p>In 1957, the eminent publisher Joseph Foret came to Salvador Dali with an impressive load of lithographic stones and the idea of creating an extraordinary set of illustrations of the famous book by Miguel Cervantes ‘Don Quichotte’. Dali used an unusual technique, which gained popularity after the book was published. Instead of pencil and paint, Dali used an air gun packed with ink. The gun shot right at the plain lithographic stone giving the basis for Dali’s inspiration. Faithful to his habits, Dalí approached this technique experimentally. For his own ‘Don Quichotte’ he did not hesitate even to dip snails in the color so that they leave traces on the stone. Therefore, the works were created spontaneously, the incipit was given by chance.<\/p>\n<p>Salvador Dalí expressed his surrealist vision of universal poetic and literary themes through his vast repertoire of images, characters, and allegories. In his characters Dalí revealed himself as an indisputable master of graphic arts, always renewing his technique, his drawings, and his colors.<\/p>\n<p>Dali, inspired by the virgin of Raphael, gives birth to his Madonna by small projections of ink and crumpled litho paper, titrated with both hands by the creator.<\/p>\n<p>Reference: “The Official Catalog of the Graphic Works of Salvador Dali” by Albert Field.<br>Ref.57-1- E, pages 123-125. Published by The Salvador Dali Archives.<\/p>\n",
            "series": "Don Quichotte",
            "publisher": None,
            "manufacturer": None,
            "canRequestLotConditionsReport": False,
            "framed": {
              "label": "Framed",
              "details": "Not included"
            },
            "signatureInfo": {
              "label": "Signature",
              "details": "Signed in the plate"
            },
            "conditionDescription": {
              "label": "Condition details",
              "details": "Very good condition"
            },
            "certificateOfAuthenticity": {
              "label": "Certificate of authenticity",
              "details": "Included"
            },
            "mediumType": {
              "__typename": "ArtworkMedium",
              "name": "Drawing, Collage or other Work on Paper",
              "longDescription": "Includes collages; drawings; figure drawing; pen and ink; sketch. This also includes paintings where paper is the support."
            },
            "articles": [],
            "literature": "<p>The Official Catalogue of The Graphic Works of Salvador Dali A.Field 57-1, p. 123<\/p>\n",
            "exhibition_history": None,
            "provenance": None,
            "image_alt": "Salvador Dalí, ‘Madonne’, 1957, Dali Paris",
            "id": "QXJ0d29yazo1ZGM2YTRkNDk2YzQ5MTAwMGU1YmIxNzA=",
            "is_saved": False,
            "images": [
              {
                "url": "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/medium.jpg",
                "internalID": "5dc6a4d5e3a4d9000e11f1b3",
                "uri": "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/large.jpg",
                "placeholder": {
                  "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=30&height=48&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FdAMtqpwtIUgN0zlJpjYrmA%2Fsmall.jpg"
                },
                "aspectRatio": 0.62,
                "is_zoomable": True,
                "is_default": True,
                "deepZoom": {
                  "Image": {
                    "xmlns": "http://schemas.microsoft.com/deepzoom/2008",
                    "Url": "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/",
                    "Format": "jpg",
                    "TileSize": 512,
                    "Overlap": 0,
                    "Size": {
                      "Width": 2500,
                      "Height": 4030
                    }
                  }
                }
              }
            ],
            "artworkMeta": {
              "share": "Check out Salvador Dalí, Madonne (1957), From Dali Paris"
            },
            "image": {
              "internalID": "5dc6a4d5e3a4d9000e11f1b3",
              "url": "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/larger.jpg",
              "height": 4030,
              "width": 2500
            },
            "is_downloadable": False,
            "is_hangable": True,
            "contextGrids": [
              {
                "__typename": "ArtistArtworkGrid",
                "title": "Other works by Salvador Dalí",
                "ctaTitle": "View all works by Salvador Dalí",
                "ctaHref": "/artist/salvador-dali",
                "artworksConnection": {
                  "edges": [
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZTdlNmRhY2QyYmQ4NDAwMTI0NjRhMDE=",
                        "slug": "salvador-dali-venus-in-the-legs",
                        "href": "/artwork/salvador-dali-venus-in-the-legs",
                        "internalID": "5e7e6dacd2bd840012464a01",
                        "image": {
                          "aspect_ratio": 0.82,
                          "placeholder": "121.39275766016712%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/wcWxq_WX2tWjO9ejZxnA7Q/large.jpg"
                        },
                        "title": "Venus in the Legs",
                        "image_title": "Salvador Dalí, ‘Venus in the Legs’, 1964",
                        "date": "1964",
                        "sale_message": "Contact For Price",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "New River Fine Art",
                          "href": "/new-river-fine-art",
                          "id": "UGFydG5lcjo1OTc2NjIxNDhiM2I4MTFhNzExMzlkOTQ=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZThjZGYxOTk0YzBiMTAwMGQ4YzcwYWM=",
                        "slug": "salvador-dali-trajan-horse-1",
                        "href": "/artwork/salvador-dali-trajan-horse-1",
                        "internalID": "5e8cdf1994c0b1000d8c70ac",
                        "image": {
                          "aspect_ratio": 1.17,
                          "placeholder": "85.16666666666667%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/ZFPyxzkl2NszlHOWdliEEA/large.jpg"
                        },
                        "title": "Trajan Horse",
                        "image_title": "Salvador Dalí, ‘Trajan Horse’, 1981",
                        "date": "1981",
                        "sale_message": None,
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Heritage Auctions",
                          "href": "/auction/partner-595e67cab202a301c4818569",
                          "id": "UGFydG5lcjo1OTVlNjdjYWIyMDJhMzAxYzQ4MTg1Njk=",
                          "type": "Auction House"
                        },
                        "sale": {
                          "is_auction": True,
                          "is_closed": True,
                          "id": "U2FsZTo1ZThjZGMwYTQxMGIxNTAwMTE3MjM2Nzk=",
                          "is_live_open": False,
                          "is_open": False,
                          "is_preview": False,
                          "display_timely_at": None
                        },
                        "sale_artwork": {
                          "counts": {
                            "bidder_positions": 2
                          },
                          "highest_bid": {
                            "display": "$700"
                          },
                          "opening_bid": {
                            "display": "$650"
                          },
                          "id": "U2FsZUFydHdvcms6NWU4Y2RmMWI5Zjc4YzAwMDEwMWYwNGI3"
                        },
                        "is_inquireable": False,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZjY2ODNlYmU1ZGViYjAwMTI2ZjU0Y2Y=",
                        "slug": "salvador-dali-mythology-leda-and-swan-leda-et-le-cygne",
                        "href": "/artwork/salvador-dali-mythology-leda-and-swan-leda-et-le-cygne",
                        "internalID": "5f6683ebe5debb00126f54cf",
                        "image": {
                          "aspect_ratio": 0.81,
                          "placeholder": "123.66666666666666%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/R6_-VNUT5fbrXUHJDPD1fQ/large.jpg"
                        },
                        "title": "Mythology: Leda and Swan - Leda Et Le Cygne ",
                        "image_title": "Salvador Dalí, ‘Mythology: Leda and Swan - Leda Et Le Cygne ’, 1963-1965",
                        "date": "1963-1965",
                        "sale_message": "Contact For Price",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Off The Wall Gallery",
                          "href": "/off-the-wall-gallery",
                          "id": "UGFydG5lcjo1OTBjZDlkYTEzOWIyMTIwMzBjYmQ0YjI=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZDVjMjM2NmZhYThkMDAwMTFkMWRlNDE=",
                        "slug": "salvador-dali-the-ballet-of-the-flowers-1",
                        "href": "/artwork/salvador-dali-the-ballet-of-the-flowers-1",
                        "internalID": "5d5c2366faa8d00011d1de41",
                        "image": {
                          "aspect_ratio": 0.76,
                          "placeholder": "131.17621337997377%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/O88NczcNfnBWiqYps8OQOA/large.jpg"
                        },
                        "title": "The Ballet of the Flowers",
                        "image_title": "Salvador Dalí, ‘The Ballet of the Flowers’, 1980",
                        "date": "1980",
                        "sale_message": None,
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Heritage Auctions",
                          "href": "/auction/partner-595e67cab202a301c4818569",
                          "id": "UGFydG5lcjo1OTVlNjdjYWIyMDJhMzAxYzQ4MTg1Njk=",
                          "type": "Auction House"
                        },
                        "sale": {
                          "is_auction": True,
                          "is_closed": True,
                          "id": "U2FsZTo1ZDVjMGZlMTAzZDlkNTAwMTI3ZTZlYjM=",
                          "is_live_open": False,
                          "is_open": False,
                          "is_preview": False,
                          "display_timely_at": None
                        },
                        "sale_artwork": {
                          "counts": {
                            "bidder_positions": 7
                          },
                          "highest_bid": {
                            "display": "$1,600"
                          },
                          "opening_bid": {
                            "display": "$650"
                          },
                          "id": "U2FsZUFydHdvcms6NWQ1YzIzNjYwM2Q5ZDUwMDEyN2U3MWVk"
                        },
                        "is_inquireable": False,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZDVjMjM2OGZhYThkMDAwMGRmMGNhMWQ=",
                        "slug": "salvador-dali-dali-dreams-1",
                        "href": "/artwork/salvador-dali-dali-dreams-1",
                        "internalID": "5d5c2368faa8d0000df0ca1d",
                        "image": {
                          "aspect_ratio": 0.72,
                          "placeholder": "138.95321908290876%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/A6kxC0Qupe4fKBfCvtMx7A/large.jpg"
                        },
                        "title": "Dali Dreams",
                        "image_title": "Salvador Dalí, ‘Dali Dreams’, 1978",
                        "date": "1978",
                        "sale_message": None,
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Heritage Auctions",
                          "href": "/auction/partner-595e67cab202a301c4818569",
                          "id": "UGFydG5lcjo1OTVlNjdjYWIyMDJhMzAxYzQ4MTg1Njk=",
                          "type": "Auction House"
                        },
                        "sale": {
                          "is_auction": True,
                          "is_closed": True,
                          "id": "U2FsZTo1ZDVjMGZlMTAzZDlkNTAwMTI3ZTZlYjM=",
                          "is_live_open": False,
                          "is_open": False,
                          "is_preview": False,
                          "display_timely_at": None
                        },
                        "sale_artwork": {
                          "counts": {
                            "bidder_positions": 3
                          },
                          "highest_bid": {
                            "display": "$800"
                          },
                          "opening_bid": {
                            "display": "$650"
                          },
                          "id": "U2FsZUFydHdvcms6NWQ1YzIzNjkwM2Q5ZDUwMDBlYzM2N2Zj"
                        },
                        "is_inquireable": False,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZDVjMjM2YjhhOTc4YTAwMTNiZmQ5YzM=",
                        "slug": "salvador-dali-anenome-per-anti-pasti-from-florals",
                        "href": "/artwork/salvador-dali-anenome-per-anti-pasti-from-florals",
                        "internalID": "5d5c236b8a978a0013bfd9c3",
                        "image": {
                          "aspect_ratio": 0.73,
                          "placeholder": "137.29977116704805%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/QKfpwK-U19W75dofj7XwDw/large.jpg"
                        },
                        "title": "Anenome per anti-pasti, from Florals",
                        "image_title": "Salvador Dalí, ‘Anenome per anti-pasti, from Florals’, 1972",
                        "date": "1972",
                        "sale_message": None,
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Heritage Auctions",
                          "href": "/auction/partner-595e67cab202a301c4818569",
                          "id": "UGFydG5lcjo1OTVlNjdjYWIyMDJhMzAxYzQ4MTg1Njk=",
                          "type": "Auction House"
                        },
                        "sale": {
                          "is_auction": True,
                          "is_closed": True,
                          "id": "U2FsZTo1ZDVjMGZlMTAzZDlkNTAwMTI3ZTZlYjM=",
                          "is_live_open": False,
                          "is_open": False,
                          "is_preview": False,
                          "display_timely_at": None
                        },
                        "sale_artwork": {
                          "counts": {
                            "bidder_positions": 17
                          },
                          "highest_bid": {
                            "display": "$700"
                          },
                          "opening_bid": {
                            "display": "$240"
                          },
                          "id": "U2FsZUFydHdvcms6NWQ1YzIzNmI5Mzg3NDEwMDBlYjFkZGQ5"
                        },
                        "is_inquireable": False,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1YmQzNWQ0MmQ0NzQxMTRiOGJiMTk1MzU=",
                        "slug": "salvador-dali-bande-de-moebius",
                        "href": "/artwork/salvador-dali-bande-de-moebius",
                        "internalID": "5bd35d42d474114b8bb19535",
                        "image": {
                          "aspect_ratio": 0.75,
                          "placeholder": "133.33333333333331%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/1dcDPcLDrgfO01mBL-vcbA/large.jpg"
                        },
                        "title": "Bande de Moëbius",
                        "image_title": "Salvador Dalí, ‘Bande de Moëbius’, 1970",
                        "date": "1970",
                        "sale_message": None,
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Capsule Gallery Auction",
                          "href": "/auction/capsule-gallery-auction",
                          "id": "UGFydG5lcjo1YWUxNmUwYTljMThkYjRjMTc3YzZhN2M=",
                          "type": "Auction House"
                        },
                        "sale": {
                          "is_auction": True,
                          "is_closed": True,
                          "id": "U2FsZTo1YmQzM2QwZTM0NDc4NjE4ZjA1MTQ4YjY=",
                          "is_live_open": False,
                          "is_open": False,
                          "is_preview": False,
                          "display_timely_at": None
                        },
                        "sale_artwork": {
                          "counts": {
                            "bidder_positions": 2
                          },
                          "highest_bid": {
                            "display": "$750"
                          },
                          "opening_bid": {
                            "display": "$700"
                          },
                          "id": "U2FsZUFydHdvcms6NWJkMzVkNDRjMjc1MWExZjA2NjI3ZjE2"
                        },
                        "is_inquireable": False,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1OTU2OWU3YWEwOWE2NzVhZTUyM2VkYTc=",
                        "slug": "salvador-dali-hippies-suite-femmes-fleurs-au-piano",
                        "href": "/artwork/salvador-dali-hippies-suite-femmes-fleurs-au-piano",
                        "internalID": "59569e7aa09a675ae523eda7",
                        "image": {
                          "aspect_ratio": 0.82,
                          "placeholder": "121.97957027122226%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/CchA583uR2qS2hBC-Atjdw/large.jpg"
                        },
                        "title": "Hippies Suite: Femmes Fleurs Au Piano ",
                        "image_title": "Salvador Dalí, ‘Hippies Suite: Femmes Fleurs Au Piano ’, 1973",
                        "date": "1973",
                        "sale_message": "Contact For Price",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Off The Wall Gallery",
                          "href": "/off-the-wall-gallery",
                          "id": "UGFydG5lcjo1OTBjZDlkYTEzOWIyMTIwMzBjYmQ0YjI=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    }
                  ]
                }
              },
              {
                "__typename": "PartnerArtworkGrid",
                "title": "Other works from Dali Paris",
                "ctaTitle": "View all works from Dali Paris",
                "ctaHref": "/dali-paris",
                "artworksConnection": {
                  "edges": [
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo2MDA4NDQ2MTg1YmRiYTU0YmI0YzQzMTM=",
                        "slug": "salvador-dali-isis-porte-portrait",
                        "href": "/artwork/salvador-dali-isis-porte-portrait",
                        "internalID": "6008446185bdba54bb4c4313",
                        "image": {
                          "aspect_ratio": 0.75,
                          "placeholder": "133.33333333333331%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/hk5-f0dhEOLgyC3TGmbygQ/large.jpg"
                        },
                        "title": "Isis Porte portrait",
                        "image_title": "Salvador Dalí, ‘Isis Porte portrait’, 1967",
                        "date": "1967",
                        "sale_message": "€80,000 - 130,000",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Dali Paris",
                          "href": "/dali-paris",
                          "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo2MDA2YTNkZDZhMDI0OTIxZWJjYmE3M2E=",
                        "slug": "salvador-dali-down-the-rabbit-hole-1",
                        "href": "/artwork/salvador-dali-down-the-rabbit-hole-1",
                        "internalID": "6006a3dd6a024921ebcba73a",
                        "image": {
                          "aspect_ratio": 0.68,
                          "placeholder": "147.54098360655738%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/GizR4ZGOQUr3iQHDSy25YQ/large.jpg"
                        },
                        "title": "Down the rabbit hole",
                        "image_title": "Salvador Dalí, ‘Down the rabbit hole’, 1969",
                        "date": "1969",
                        "sale_message": "€2,500 - 5,000",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Dali Paris",
                          "href": "/dali-paris",
                          "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZjdmMWEyODM0YjY5MTAwMGU3ZTYwZmY=",
                        "slug": "salvador-dali-chinese-roquin",
                        "href": "/artwork/salvador-dali-chinese-roquin",
                        "internalID": "5f7f1a2834b691000e7e60ff",
                        "image": {
                          "aspect_ratio": 0.71,
                          "placeholder": "141.47027787548365%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/JBR7r726XJxG46C2YIa99w/large.jpg"
                        },
                        "title": "Chinese Roquin",
                        "image_title": "Salvador Dalí, ‘Chinese Roquin’, 1973",
                        "date": "1973",
                        "sale_message": "€2,500 - 5,000",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Dali Paris",
                          "href": "/dali-paris",
                          "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZjdlZWFkM2YxNjE0YjAwMGRmNGRmNjk=",
                        "slug": "salvador-dali-leg-tribute-ceremonial",
                        "href": "/artwork/salvador-dali-leg-tribute-ceremonial",
                        "internalID": "5f7eead3f1614b000df4df69",
                        "image": {
                          "aspect_ratio": 0.69,
                          "placeholder": "144.04934687953556%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/6LtY0VCqQtGiyVv0pR069w/large.jpg"
                        },
                        "title": "Leg Tribute Ceremonial",
                        "image_title": "Salvador Dalí, ‘Leg Tribute Ceremonial’, 1973",
                        "date": "1973",
                        "sale_message": "€2,500 - 5,000",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Dali Paris",
                          "href": "/dali-paris",
                          "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZjZmMTViODViMmQ2MDAwMGUxMWMwZDU=",
                        "slug": "salvador-dali-familiar-phallus",
                        "href": "/artwork/salvador-dali-familiar-phallus",
                        "internalID": "5f6f15b85b2d60000e11c0d5",
                        "image": {
                          "aspect_ratio": 0.69,
                          "placeholder": "143.89285714285714%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/Xdme27n_bOge93qS974V0w/large.jpg"
                        },
                        "title": "Familiar Phallus",
                        "image_title": "Salvador Dalí, ‘Familiar Phallus’, 1973",
                        "date": "1973",
                        "sale_message": "€2,500 - 5,000",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Dali Paris",
                          "href": "/dali-paris",
                          "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZjZmMTM2ODgwZmNkNzAwMGRjZDE4Nzg=",
                        "slug": "salvador-dali-giant-pastry-cook",
                        "href": "/artwork/salvador-dali-giant-pastry-cook",
                        "internalID": "5f6f136880fcd7000dcd1878",
                        "image": {
                          "aspect_ratio": 0.7,
                          "placeholder": "143.2442328817283%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/H4Q9pEzdntUWtyS2w-JFUw/large.jpg"
                        },
                        "title": "Giant Pastry Cook",
                        "image_title": "Salvador Dalí, ‘Giant Pastry Cook’, 1973",
                        "date": "1973",
                        "sale_message": "€2,500 - 5,000",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Dali Paris",
                          "href": "/dali-paris",
                          "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZjY3MjgyNzI0Mzg3MTAwMGVhM2EzMDQ=",
                        "slug": "salvador-dali-faith-moves-mountains",
                        "href": "/artwork/salvador-dali-faith-moves-mountains",
                        "internalID": "5f672827243871000ea3a304",
                        "image": {
                          "aspect_ratio": 0.73,
                          "placeholder": "136.58854166666669%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/jWwejI8rFSIwAW2WxkOq1A/large.jpg"
                        },
                        "title": "Faith Moves Mountains",
                        "image_title": "Salvador Dalí, ‘Faith Moves Mountains’, 1959",
                        "date": "1959",
                        "sale_message": "€1,000 - 2,500",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Dali Paris",
                          "href": "/dali-paris",
                          "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZjQ5MGMyN2JjNzFiODAwMGZkNTM5MTA=",
                        "slug": "salvador-dali-bell-figure",
                        "href": "/artwork/salvador-dali-bell-figure",
                        "internalID": "5f490c27bc71b8000fd53910",
                        "image": {
                          "aspect_ratio": 0.71,
                          "placeholder": "140.76704545454547%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/2ZxTfbmthsGkr126SyFDtw/large.jpg"
                        },
                        "title": "Bell Figure",
                        "image_title": "Salvador Dalí, ‘Bell Figure’, 1973",
                        "date": "1973",
                        "sale_message": "€2,500 - 5,000",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                            "href": "/artist/salvador-dali",
                            "name": "Salvador Dalí"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Dali Paris",
                          "href": "/dali-paris",
                          "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    }
                  ]
                }
              },
              {
                "__typename": "RelatedArtworkGrid",
                "title": "Related works",
                "ctaTitle": None,
                "ctaHref": None,
                "artworksConnection": {
                  "edges": [
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1YjdmZDQxZWYzNDc0NTBiNjQ1N2UzMDI=",
                        "slug": "joan-miro-les-essencies-de-la-terra-14",
                        "href": "/artwork/joan-miro-les-essencies-de-la-terra-14",
                        "internalID": "5b7fd41ef347450b6457e302",
                        "image": {
                          "aspect_ratio": 1.45,
                          "placeholder": "69.04296875%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/wqPwOfJoTo-b1zFpRxnczA/large.jpg"
                        },
                        "title": "Les Essències de la Terra",
                        "image_title": "Joan Miró, ‘Les Essències de la Terra’, 1968",
                        "date": "1968",
                        "sale_message": "€650",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                            "href": "/artist/joan-miro",
                            "name": "Joan Miró"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Wallector",
                          "href": "/wallector",
                          "id": "UGFydG5lcjo1OTU2Njk5ZDJhODkzYTZiNDYwNjk0ZDM=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1ZWRlMjQ5ODM1YzQ0NzAwMTJlODg2NTg=",
                        "slug": "pablo-picasso-profils-et-tetes",
                        "href": "/artwork/pablo-picasso-profils-et-tetes",
                        "internalID": "5ede249835c4470012e88658",
                        "image": {
                          "aspect_ratio": 1.5,
                          "placeholder": "66.66666666666666%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/Y1NlSs2GNBqE9Or7AYfxCw/large.jpg"
                        },
                        "title": "Profils et Têtes",
                        "image_title": "Pablo Picasso, ‘Profils et Têtes’, 1967",
                        "date": "1967",
                        "sale_message": "Contact For Price",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkOGI5MjhiNGViNjhhMWIyYzAwMDFmMg==",
                            "href": "/artist/pablo-picasso",
                            "name": "Pablo Picasso"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Piano Nobile",
                          "href": "/piano-nobile",
                          "id": "UGFydG5lcjo1NTMwNDBlZDc3NmY3MjM2MDM2NTAzMDA=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1YTdhMWFkYzhiMGMxNDA5NjQ4NmZlYTg=",
                        "slug": "after-joan-miro-atelier-mourlot-1967",
                        "href": "/artwork/after-joan-miro-atelier-mourlot-1967",
                        "internalID": "5a7a1adc8b0c14096486fea8",
                        "image": {
                          "aspect_ratio": 0.71,
                          "placeholder": "141.227125941873%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/BIV8j709eB78h6u0Yf6nlg/large.jpg"
                        },
                        "title": "Atelier Mourlot, 1967",
                        "image_title": "Joan Miró, ‘Atelier Mourlot, 1967’, 1967",
                        "date": "1967",
                        "sale_message": None,
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                            "href": "/artist/joan-miro",
                            "name": "Joan Miró"
                          },
                          {
                            "id": "QXJ0aXN0OjRkZGU3MGExMzA2ZjY4MDAwMTAwMzZlZg==",
                            "href": "/artist/alexander-calder",
                            "name": "Alexander Calder"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Forum Auctions",
                          "href": "/auction/forum-auctions",
                          "id": "UGFydG5lcjo1OTVlNjdhNWM5ZGMyNDFiZThjYjQyNDU=",
                          "type": "Auction House"
                        },
                        "sale": {
                          "is_auction": True,
                          "is_closed": True,
                          "id": "U2FsZTo1YTdhMTgwODc2MjJkZDQ5ZDZkYzQ5MTY=",
                          "is_live_open": False,
                          "is_open": False,
                          "is_preview": False,
                          "display_timely_at": None
                        },
                        "sale_artwork": {
                          "counts": {
                            "bidder_positions": 0
                          },
                          "highest_bid": {
                            "display": None
                          },
                          "opening_bid": {
                            "display": "£180"
                          },
                          "id": "U2FsZUFydHdvcms6NWE3YTFhZGVjZDUzMGU0OGQ5NDk2Nzgy"
                        },
                        "is_inquireable": False,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1YWY1ZjZiZmNiNGMyNzU5ZTI5NjI3YzY=",
                        "slug": "eduardo-chillida-untitled-2-1",
                        "href": "/artwork/eduardo-chillida-untitled-2-1",
                        "internalID": "5af5f6bfcb4c2759e29627c6",
                        "image": {
                          "aspect_ratio": 1.21,
                          "placeholder": "82.6%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/7ZWbJOz3-xVf8WKfrtlwPg/large.jpg"
                        },
                        "title": "Untitled 2",
                        "image_title": "Eduardo Chillida, ‘Untitled 2’, 1961",
                        "date": "1961",
                        "sale_message": "Sold",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRlOTczNWRkN2QxNDJjMDAwMTAwMGYzYw==",
                            "href": "/artist/eduardo-chillida",
                            "name": "Eduardo Chillida"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Baterbys",
                          "href": "/baterbys",
                          "id": "UGFydG5lcjo1OGVkNDg5ZGM5ZGMyNDIzOTcxMjY3NTQ=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1YTNlYzMyNzljMThkYjAyZTU5ZWIwNTQ=",
                        "slug": "joan-miro-les-guetteurs-the-watchers-and-batteuse-paysage-champagne",
                        "href": "/artwork/joan-miro-les-guetteurs-the-watchers-and-batteuse-paysage-champagne",
                        "internalID": "5a3ec3279c18db02e59eb054",
                        "image": {
                          "aspect_ratio": 0.69,
                          "placeholder": "144.39655172413794%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/_SFek7sm7wdF7AhRyISwgg/large.jpg"
                        },
                        "title": "Les Guetteurs (The Watchers); and Batteuse Paysage Champagne",
                        "image_title": "Joan Miró, ‘Les Guetteurs (The Watchers); and Batteuse Paysage Champagne’, 1964; and 1954",
                        "date": "1964; and 1954",
                        "sale_message": None,
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                            "href": "/artist/joan-miro",
                            "name": "Joan Miró"
                          },
                          {
                            "id": "QXJ0aXN0OjRlOTU5Yjc4Yzg4OTA4MDAwMTAwNjI5Zg==",
                            "href": "/artist/raoul-dufy",
                            "name": "Raoul Dufy"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Phillips",
                          "href": "/auction/phillips-1",
                          "id": "UGFydG5lcjo1OTVlNjhhNmIyMDJhMzAxYzQ4MTg1OGQ=",
                          "type": "Auction House"
                        },
                        "sale": {
                          "is_auction": True,
                          "is_closed": True,
                          "id": "U2FsZTo1YTM4NDE0Y2M5ZGMyNDVjMmI1ZTA2OTI=",
                          "is_live_open": False,
                          "is_open": False,
                          "is_preview": False,
                          "display_timely_at": None
                        },
                        "sale_artwork": {
                          "counts": {
                            "bidder_positions": 2
                          },
                          "highest_bid": {
                            "display": "£1,300"
                          },
                          "opening_bid": {
                            "display": "£1,200"
                          },
                          "id": "U2FsZUFydHdvcms6NWEzZWMzMjcyYTg5M2EwNWQ3Y2I1MGNk"
                        },
                        "is_inquireable": False,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1YTc5YjgwOTc2MjJkZDQ4Y2RiZDY4YTA=",
                        "slug": "antoni-tapies-trois-gris-et-marron",
                        "href": "/artwork/antoni-tapies-trois-gris-et-marron",
                        "internalID": "5a79b8097622dd48cdbd68a0",
                        "image": {
                          "aspect_ratio": 0.71,
                          "placeholder": "141.12458654906283%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/8JPbx4e0QwmOkywQbKmaUw/large.jpg"
                        },
                        "title": "Trois Gris Et Marron",
                        "image_title": "Antoni Tàpies, ‘Trois Gris Et Marron’, 1967",
                        "date": "1967",
                        "sale_message": "Under €4,850",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRkYzk5MmEyOTk3NDQ2MDAwMTAwMzhiOQ==",
                            "href": "/artist/antoni-tapies",
                            "name": "Antoni Tàpies"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Kunzt Gallery",
                          "href": "/kunzt-gallery",
                          "id": "UGFydG5lcjo1OWY0OTVkYzhiMGMxNDMzMzVmNjkwNmE=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1Zjk4MmU2MjM2ZjA4MDAwMGU4YjQ3OGI=",
                        "slug": "manolo-millares-pintura-1",
                        "href": "/artwork/manolo-millares-pintura-1",
                        "internalID": "5f982e6236f080000e8b478b",
                        "image": {
                          "aspect_ratio": 1.33,
                          "placeholder": "75%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/hjTexVnxDkNkANPdV2wTjg/large.jpg"
                        },
                        "title": "Pintura",
                        "image_title": "Manolo Millares, ‘Pintura’, 1967",
                        "date": "1967",
                        "sale_message": "Contact For Price",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjUwNmIzM2RkNDQ2NjE3MDAwMjAwMTNhMg==",
                            "href": "/artist/manolo-millares",
                            "name": "Manolo Millares"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Artelandia Gallery",
                          "href": "/artelandia-gallery",
                          "id": "UGFydG5lcjo1Zjk2YWY3NjMxODdiMDAwMTEyZmJmYTg=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    },
                    {
                      "__typename": "ArtworkEdge",
                      "node": {
                        "id": "QXJ0d29yazo1NzhmNGE3NjEzOWIyMTMxN2UwMDUwOTY=",
                        "slug": "wifredo-lam-untitled-20",
                        "href": "/artwork/wifredo-lam-untitled-20",
                        "internalID": "578f4a76139b21317e005096",
                        "image": {
                          "aspect_ratio": 0.78,
                          "placeholder": "128.21659215101838%",
                          "url": "https://d32dm0rphc51dk.cloudfront.net/JfrTO8a6ScSPEXAFQC3j1w/large.jpg"
                        },
                        "title": "Untitled ",
                        "image_title": "Wifredo Lam, ‘Untitled ’, 1946",
                        "date": "1946",
                        "sale_message": "Sold",
                        "cultural_maker": None,
                        "artists": [
                          {
                            "id": "QXJ0aXN0OjRlOTc0NzdmNmJhNzEyMDAwMTAwMTY1MA==",
                            "href": "/artist/wifredo-lam",
                            "name": "Wifredo Lam"
                          }
                        ],
                        "collecting_institution": None,
                        "partner": {
                          "name": "Galerie F. Hessler",
                          "href": "/galerie-f-hessler",
                          "id": "UGFydG5lcjo1NmJhMTY5YzY2ZmQxYzY3MGIwMDAwNmQ=",
                          "type": "Gallery"
                        },
                        "sale": None,
                        "sale_artwork": None,
                        "is_inquireable": True,
                        "is_saved": False,
                        "is_biddable": False
                      }
                    }
                  ]
                }
              }
            ],
            "layers": [
              {
                "name": "Most Similar",
                "internalID": "main",
                "id": "QXJ0d29ya0xheWVyOm1haW4="
              },
              {
                "name": "For Sale",
                "internalID": "for-sale",
                "id": "QXJ0d29ya0xheWVyOmZvci1zYWxl"
              }
            ],
            "layer": {
              "name": "Most Similar",
              "artworksConnection": {
                "edges": [
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YjdmZDQxZWYzNDc0NTBiNjQ1N2UzMDI=",
                      "slug": "joan-miro-les-essencies-de-la-terra-14",
                      "href": "/artwork/joan-miro-les-essencies-de-la-terra-14",
                      "internalID": "5b7fd41ef347450b6457e302",
                      "image": {
                        "aspect_ratio": 1.45,
                        "placeholder": "69.04296875%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/wqPwOfJoTo-b1zFpRxnczA/large.jpg"
                      },
                      "title": "Les Essències de la Terra",
                      "image_title": "Joan Miró, ‘Les Essències de la Terra’, 1968",
                      "date": "1968",
                      "sale_message": "€650",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                          "href": "/artist/joan-miro",
                          "name": "Joan Miró"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Wallector",
                        "href": "/wallector",
                        "id": "UGFydG5lcjo1OTU2Njk5ZDJhODkzYTZiNDYwNjk0ZDM=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZWRlMjQ5ODM1YzQ0NzAwMTJlODg2NTg=",
                      "slug": "pablo-picasso-profils-et-tetes",
                      "href": "/artwork/pablo-picasso-profils-et-tetes",
                      "internalID": "5ede249835c4470012e88658",
                      "image": {
                        "aspect_ratio": 1.5,
                        "placeholder": "66.66666666666666%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/Y1NlSs2GNBqE9Or7AYfxCw/large.jpg"
                      },
                      "title": "Profils et Têtes",
                      "image_title": "Pablo Picasso, ‘Profils et Têtes’, 1967",
                      "date": "1967",
                      "sale_message": "Contact For Price",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkOGI5MjhiNGViNjhhMWIyYzAwMDFmMg==",
                          "href": "/artist/pablo-picasso",
                          "name": "Pablo Picasso"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Piano Nobile",
                        "href": "/piano-nobile",
                        "id": "UGFydG5lcjo1NTMwNDBlZDc3NmY3MjM2MDM2NTAzMDA=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YTdhMWFkYzhiMGMxNDA5NjQ4NmZlYTg=",
                      "slug": "after-joan-miro-atelier-mourlot-1967",
                      "href": "/artwork/after-joan-miro-atelier-mourlot-1967",
                      "internalID": "5a7a1adc8b0c14096486fea8",
                      "image": {
                        "aspect_ratio": 0.71,
                        "placeholder": "141.227125941873%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/BIV8j709eB78h6u0Yf6nlg/large.jpg"
                      },
                      "title": "Atelier Mourlot, 1967",
                      "image_title": "Joan Miró, ‘Atelier Mourlot, 1967’, 1967",
                      "date": "1967",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                          "href": "/artist/joan-miro",
                          "name": "Joan Miró"
                        },
                        {
                          "id": "QXJ0aXN0OjRkZGU3MGExMzA2ZjY4MDAwMTAwMzZlZg==",
                          "href": "/artist/alexander-calder",
                          "name": "Alexander Calder"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Forum Auctions",
                        "href": "/auction/forum-auctions",
                        "id": "UGFydG5lcjo1OTVlNjdhNWM5ZGMyNDFiZThjYjQyNDU=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1YTdhMTgwODc2MjJkZDQ5ZDZkYzQ5MTY=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 0
                        },
                        "highest_bid": {
                          "display": None
                        },
                        "opening_bid": {
                          "display": "£180"
                        },
                        "id": "U2FsZUFydHdvcms6NWE3YTFhZGVjZDUzMGU0OGQ5NDk2Nzgy"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YWY1ZjZiZmNiNGMyNzU5ZTI5NjI3YzY=",
                      "slug": "eduardo-chillida-untitled-2-1",
                      "href": "/artwork/eduardo-chillida-untitled-2-1",
                      "internalID": "5af5f6bfcb4c2759e29627c6",
                      "image": {
                        "aspect_ratio": 1.21,
                        "placeholder": "82.6%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/7ZWbJOz3-xVf8WKfrtlwPg/large.jpg"
                      },
                      "title": "Untitled 2",
                      "image_title": "Eduardo Chillida, ‘Untitled 2’, 1961",
                      "date": "1961",
                      "sale_message": "Sold",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRlOTczNWRkN2QxNDJjMDAwMTAwMGYzYw==",
                          "href": "/artist/eduardo-chillida",
                          "name": "Eduardo Chillida"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Baterbys",
                        "href": "/baterbys",
                        "id": "UGFydG5lcjo1OGVkNDg5ZGM5ZGMyNDIzOTcxMjY3NTQ=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YTNlYzMyNzljMThkYjAyZTU5ZWIwNTQ=",
                      "slug": "joan-miro-les-guetteurs-the-watchers-and-batteuse-paysage-champagne",
                      "href": "/artwork/joan-miro-les-guetteurs-the-watchers-and-batteuse-paysage-champagne",
                      "internalID": "5a3ec3279c18db02e59eb054",
                      "image": {
                        "aspect_ratio": 0.69,
                        "placeholder": "144.39655172413794%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/_SFek7sm7wdF7AhRyISwgg/large.jpg"
                      },
                      "title": "Les Guetteurs (The Watchers); and Batteuse Paysage Champagne",
                      "image_title": "Joan Miró, ‘Les Guetteurs (The Watchers); and Batteuse Paysage Champagne’, 1964; and 1954",
                      "date": "1964; and 1954",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                          "href": "/artist/joan-miro",
                          "name": "Joan Miró"
                        },
                        {
                          "id": "QXJ0aXN0OjRlOTU5Yjc4Yzg4OTA4MDAwMTAwNjI5Zg==",
                          "href": "/artist/raoul-dufy",
                          "name": "Raoul Dufy"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Phillips",
                        "href": "/auction/phillips-1",
                        "id": "UGFydG5lcjo1OTVlNjhhNmIyMDJhMzAxYzQ4MTg1OGQ=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1YTM4NDE0Y2M5ZGMyNDVjMmI1ZTA2OTI=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 2
                        },
                        "highest_bid": {
                          "display": "£1,300"
                        },
                        "opening_bid": {
                          "display": "£1,200"
                        },
                        "id": "U2FsZUFydHdvcms6NWEzZWMzMjcyYTg5M2EwNWQ3Y2I1MGNk"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YTc5YjgwOTc2MjJkZDQ4Y2RiZDY4YTA=",
                      "slug": "antoni-tapies-trois-gris-et-marron",
                      "href": "/artwork/antoni-tapies-trois-gris-et-marron",
                      "internalID": "5a79b8097622dd48cdbd68a0",
                      "image": {
                        "aspect_ratio": 0.71,
                        "placeholder": "141.12458654906283%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/8JPbx4e0QwmOkywQbKmaUw/large.jpg"
                      },
                      "title": "Trois Gris Et Marron",
                      "image_title": "Antoni Tàpies, ‘Trois Gris Et Marron’, 1967",
                      "date": "1967",
                      "sale_message": "Under €4,850",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYzk5MmEyOTk3NDQ2MDAwMTAwMzhiOQ==",
                          "href": "/artist/antoni-tapies",
                          "name": "Antoni Tàpies"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Kunzt Gallery",
                        "href": "/kunzt-gallery",
                        "id": "UGFydG5lcjo1OWY0OTVkYzhiMGMxNDMzMzVmNjkwNmE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1Zjk4MmU2MjM2ZjA4MDAwMGU4YjQ3OGI=",
                      "slug": "manolo-millares-pintura-1",
                      "href": "/artwork/manolo-millares-pintura-1",
                      "internalID": "5f982e6236f080000e8b478b",
                      "image": {
                        "aspect_ratio": 1.33,
                        "placeholder": "75%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/hjTexVnxDkNkANPdV2wTjg/large.jpg"
                      },
                      "title": "Pintura",
                      "image_title": "Manolo Millares, ‘Pintura’, 1967",
                      "date": "1967",
                      "sale_message": "Contact For Price",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjUwNmIzM2RkNDQ2NjE3MDAwMjAwMTNhMg==",
                          "href": "/artist/manolo-millares",
                          "name": "Manolo Millares"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Artelandia Gallery",
                        "href": "/artelandia-gallery",
                        "id": "UGFydG5lcjo1Zjk2YWY3NjMxODdiMDAwMTEyZmJmYTg=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1NzhmNGE3NjEzOWIyMTMxN2UwMDUwOTY=",
                      "slug": "wifredo-lam-untitled-20",
                      "href": "/artwork/wifredo-lam-untitled-20",
                      "internalID": "578f4a76139b21317e005096",
                      "image": {
                        "aspect_ratio": 0.78,
                        "placeholder": "128.21659215101838%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/JfrTO8a6ScSPEXAFQC3j1w/large.jpg"
                      },
                      "title": "Untitled ",
                      "image_title": "Wifredo Lam, ‘Untitled ’, 1946",
                      "date": "1946",
                      "sale_message": "Sold",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRlOTc0NzdmNmJhNzEyMDAwMTAwMTY1MA==",
                          "href": "/artist/wifredo-lam",
                          "name": "Wifredo Lam"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Galerie F. Hessler",
                        "href": "/galerie-f-hessler",
                        "id": "UGFydG5lcjo1NmJhMTY5YzY2ZmQxYzY3MGIwMDAwNmQ=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  }
                ]
              },
              "id": "QXJ0d29ya0xheWVyOm1haW4="
            },
            "artistSeriesConnection": {
              "edges": []
            },
            "seriesArtist": {
              "artistSeriesConnection": {
                "edges": [
                  {
                    "node": {
                      "internalID": "0d38ea83-2e16-4846-ac76-7e6a96b723b6",
                      "title": "The Divine Comedy",
                      "slug": "salvador-dali-the-divine-comedy",
                      "featured": False,
                      "artworksCountMessage": "373 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FGGZPqjDTpQGur2lsqFeUww%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "f980c925-3f4c-4d26-af45-ba0f2ae5fa22",
                      "title": "Don Quixote",
                      "slug": "salvador-dali-don-quixote",
                      "featured": False,
                      "artworksCountMessage": "46 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FE1Ulk9KJ0iQIRZDlyehbEw%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "67b5a464-51a3-419b-87d1-b788313cacd4",
                      "title": "Venus",
                      "slug": "salvador-dali-venus",
                      "featured": False,
                      "artworksCountMessage": "40 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FwcWxq_WX2tWjO9ejZxnA7Q%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "c1da431c-426f-4e95-ac86-b8ec064a653b",
                      "title": "The Bible",
                      "slug": "salvador-dali-the-bible",
                      "featured": False,
                      "artworksCountMessage": "38 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FEprKIL3UATLdoMD4ea6XMg%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "5cae3bd1-1516-4481-84f2-6e81c17cf3b9",
                      "title": "Dante",
                      "slug": "salvador-dali-dante",
                      "featured": False,
                      "artworksCountMessage": "37 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FlglZ8nT2AYzDwwVW_JVj2g%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "2f1828bc-90be-4b49-8b65-4f82427ca905",
                      "title": "Mythologies",
                      "slug": "salvador-dali-mythologies",
                      "featured": False,
                      "artworksCountMessage": "31 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F8iNBtjqbTL-WKRzvZYuKCg%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "7bd85620-eafc-4d97-9ad0-231835704199",
                      "title": "Fruits",
                      "slug": "salvador-dali-fruits",
                      "featured": False,
                      "artworksCountMessage": "29 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FQKfpwK-U19W75dofj7XwDw%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "0eb82c98-6a9d-4b32-a20e-8918e1338ff6",
                      "title": "Signs of the Zodiac",
                      "slug": "salvador-dali-signs-of-the-zodiac",
                      "featured": False,
                      "artworksCountMessage": "24 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fb1cKQL8IvN3yIT5fFQtE5Q%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "9a675bdb-0ea4-4be0-a720-f7d37a9ad4ca",
                      "title": "Faust",
                      "slug": "salvador-dali-faust",
                      "featured": False,
                      "artworksCountMessage": "23 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FMJqf4fQIo3skVUYi0W_2pw%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "08994a70-aeb1-4d00-8f14-7345735dd0f7",
                      "title": "Melting Clocks",
                      "slug": "salvador-dali-melting-clocks",
                      "featured": False,
                      "artworksCountMessage": "21 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FCJ-ZqbPozMkY4bQTuj5tuQ%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "6ca2b8ff-99cd-464a-b003-315667dd254a",
                      "title": "Elephants",
                      "slug": "salvador-dali-elephants",
                      "featured": False,
                      "artworksCountMessage": "18 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FWRWLhRJzxS0RYPEc4NsY4g%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "899af2f6-bd5b-4721-a6fd-32767b10a5b9",
                      "title": "Les Amours de Cassandre",
                      "slug": "salvador-dali-les-amours-de-cassandre",
                      "featured": False,
                      "artworksCountMessage": "15 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FmGl0zjCljOVEcxBr_h3POA%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "8e7668a0-10dd-4a8d-93ea-72413cb08297",
                      "title": "Shakespeare",
                      "slug": "salvador-dali-shakespeare",
                      "featured": False,
                      "artworksCountMessage": "14 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F8jZnKiSRgw0zyAPp0c3c9A%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "c5f22dfe-39b3-4a9f-bae4-ab497239320c",
                      "title": "Butterflies",
                      "slug": "salvador-dali-butterflies",
                      "featured": False,
                      "artworksCountMessage": "14 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FEqob_SW84ji3Tc7ClSoonQ%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "19473968-9fe8-4e4d-b2d1-ed222ebbdc2a",
                      "title": "Casanova",
                      "slug": "salvador-dali-casanova",
                      "featured": False,
                      "artworksCountMessage": "10 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FEbCQuJ6DX-M8_wQ9brlsuA%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "98ad6615-de31-466a-a69a-05325ff9864f",
                      "title": "Memories of Surrealism",
                      "slug": "salvador-dali-memories-of-surrealism",
                      "featured": False,
                      "artworksCountMessage": "10 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F4kOy3i3xgtE7-Lqp_FA_5g%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "6d1a5e6a-3413-498c-b21f-07dc0ee35526",
                      "title": "Lobsters",
                      "slug": "salvador-dali-lobsters",
                      "featured": False,
                      "artworksCountMessage": "8 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fp20PCKLZIfN7dkmShWn5kw%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "bffe0fd2-3410-4cc3-87aa-f554f28e1b1d",
                      "title": "Les Diners de Gala",
                      "slug": "salvador-dali-les-diners-de-gala",
                      "featured": False,
                      "artworksCountMessage": "8 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fp20PCKLZIfN7dkmShWn5kw%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "791a89d1-9ba8-4140-a931-9c328a439593",
                      "title": "Poems",
                      "slug": "salvador-dali-poems",
                      "featured": False,
                      "artworksCountMessage": "7 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FALer2U740JGmNqj0UBSrzw%2Flarge.jpg"
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "internalID": "519d9289-8296-4161-b9f7-5d4217781532",
                      "title": "Playing Cards",
                      "slug": "salvador-dali-playing-cards",
                      "featured": False,
                      "artworksCountMessage": "2 available",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FiX0wSBw4VbvCpmRggO3xUA%2Flarge.jpg"
                        }
                      }
                    }
                  }
                ]
              },
              "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg=="
            },
            "seriesForCounts": {
              "edges": []
            },
            "pricingContext": None
          },
          "me": None
        }
      },
      "data": {
        "artwork": {
          "slug": "salvador-dali-madonne",
          "internalID": "5dc6a4d496c491000e5bb170",
          "is_acquireable": False,
          "is_offerable": False,
          "availability": "for sale",
          "listPrice": {
            "__typename": "PriceRange",
            "display": "€5,000 - 7,500",
            "minPrice": {
              "major": 5000,
              "currencyCode": "EUR",
              "minor": 500000
            },
            "maxPrice": {
              "major": 7500,
              "minor": 750000
            }
          },
          "is_in_auction": False,
          "sale": None,
          "artists": [
            {
              "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
              "slug": "salvador-dali",
              "internalID": "4dadcce67129f059240009df",
              "name": "Salvador Dalí",
              "href": "/artist/salvador-dali",
              "image": {
                "cropped": {
                  "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=100&height=100&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FD8nvgg6qr0fmPkx9fzzj-Q%2Flarge.jpg"
                }
              },
              "formatted_nationality_and_birthday": "Spanish, 1904–1989",
              "counts": {
                "partner_shows": 143,
                "follows": 31759
              },
              "exhibition_highlights": [
                {
                  "partner": {
                    "__typename": "Partner",
                    "name": "Opera Gallery",
                    "id": "UGFydG5lcjo1MGQxYTcyYjEyNzIzMDgxOTcwMDA0NDU="
                  },
                  "name": "Masterpiece Collection / Singapore",
                  "start_at": "2019",
                  "cover_image": {
                    "cropped": {
                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FU9DrqRPAqDnAyaHkdmPTPQ%2Flarge.jpg"
                    }
                  },
                  "city": "Singapore",
                  "id": "U2hvdzo1ZDY3ZDdiODc4ZWVlNzAwMTM0ZjY0OGQ="
                },
                {
                  "partner": {
                    "__typename": "Partner",
                    "name": "Opera Gallery",
                    "id": "UGFydG5lcjo1MGQxYTcyYjEyNzIzMDgxOTcwMDA0NDU="
                  },
                  "name": "Salvador Dalí",
                  "start_at": "2015",
                  "cover_image": {
                    "cropped": {
                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FVspDps0UOe3b85_H7mSexw%2Flarge.jpg"
                    }
                  },
                  "city": "Singapore",
                  "id": "U2hvdzo1NWRmMjUwZTcyNjE2OTNkOWIwMDAwZTg="
                },
                {
                  "partner": {
                    "__typename": "Partner",
                    "name": "Kunstmuseum Bern",
                    "id": "UGFydG5lcjo1NTEzMTlhMTcyNjE2OTFmZDAwZjA5MDA="
                  },
                  "name": "Highlights from Kunstmuseum Bern",
                  "start_at": "2016",
                  "cover_image": {
                    "cropped": {
                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FNMq6w3co7aUecadVsUZnLw%2Flarge.jpg"
                    }
                  },
                  "city": "Bern",
                  "id": "U2hvdzo1NzFlODY1OGNkNTMwZTY1OTcwMDA4ODQ="
                }
              ],
              "collections": [
                "Tate",
                "Museum of Modern Art (MoMA)",
                "Indianapolis Museum of Art at Newfields",
                "de la Cruz Collection"
              ],
              "highlights": {
                "partnersConnection": {
                  "edges": []
                }
              },
              "auctionResultsConnection": {
                "edges": [
                  {
                    "node": {
                      "__typename": "AuctionResult",
                      "id": "QXVjdGlvblJlc3VsdDozMjQ0NDI5",
                      "price_realized": {
                        "display": "£13m"
                      },
                      "organization": "Sotheby's",
                      "sale_date": "2011"
                    }
                  }
                ]
              },
              "biographyBlurb": {
                "text": "<p>Salvador Dalí was a leading proponent of <a href=\"/gene/surrealism\">Surrealism<\/a>, the 20-century avant-garde movement that sought to release the creative potential of the unconscious through strange, dream-like imagery. “<a href=\"/gene/surrealism\">Surrealism<\/a> is destructive, but it destroys only what it considers to be shackles limiting our vision,” he said. Dalí is specially credited with the innovation of “paranoia-criticism,” a philosophy of art making he defined as “irrational understanding based on the interpretive-critical association of delirious phenomena.” In addition to meticulously painting fantastic compositions, such as <em>The Accommodations of Desire<\/em> (1929) and the <a href=\"/collection/salvador-dali-melting-clocks\">melting clocks<\/a> in his famed <em>The Persistence of Memory<\/em> (1931), Dalí was a prolific writer and early filmmaker, and cultivated an eccentric public persona with his flamboyant mustache, pet ocelot, and outlandish behavior and quips. <\/p>\n"
              },
              "is_followed": False,
              "related": {
                "suggestedConnection": None
              },
              "is_consignable": True
            }
          ],
          "artist": {
            "internalID": "4dadcce67129f059240009df",
            "slug": "salvador-dali",
            "name": "Salvador Dalí",
            "href": "/artist/salvador-dali",
            "image": {
              "cropped": {
                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=100&height=100&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FD8nvgg6qr0fmPkx9fzzj-Q%2Flarge.jpg"
              }
            },
            "formatted_nationality_and_birthday": "Spanish, 1904–1989",
            "counts": {
              "partner_shows": 143,
              "follows": 31759
            },
            "exhibition_highlights": [
              {
                "partner": {
                  "__typename": "Partner",
                  "name": "Opera Gallery",
                  "id": "UGFydG5lcjo1MGQxYTcyYjEyNzIzMDgxOTcwMDA0NDU="
                },
                "name": "Masterpiece Collection / Singapore",
                "start_at": "2019",
                "cover_image": {
                  "cropped": {
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FU9DrqRPAqDnAyaHkdmPTPQ%2Flarge.jpg"
                  }
                },
                "city": "Singapore",
                "id": "U2hvdzo1ZDY3ZDdiODc4ZWVlNzAwMTM0ZjY0OGQ="
              },
              {
                "partner": {
                  "__typename": "Partner",
                  "name": "Opera Gallery",
                  "id": "UGFydG5lcjo1MGQxYTcyYjEyNzIzMDgxOTcwMDA0NDU="
                },
                "name": "Salvador Dalí",
                "start_at": "2015",
                "cover_image": {
                  "cropped": {
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FVspDps0UOe3b85_H7mSexw%2Flarge.jpg"
                  }
                },
                "city": "Singapore",
                "id": "U2hvdzo1NWRmMjUwZTcyNjE2OTNkOWIwMDAwZTg="
              },
              {
                "partner": {
                  "__typename": "Partner",
                  "name": "Kunstmuseum Bern",
                  "id": "UGFydG5lcjo1NTEzMTlhMTcyNjE2OTFmZDAwZjA5MDA="
                },
                "name": "Highlights from Kunstmuseum Bern",
                "start_at": "2016",
                "cover_image": {
                  "cropped": {
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FNMq6w3co7aUecadVsUZnLw%2Flarge.jpg"
                  }
                },
                "city": "Bern",
                "id": "U2hvdzo1NzFlODY1OGNkNTMwZTY1OTcwMDA4ODQ="
              }
            ],
            "collections": [
              "Tate",
              "Museum of Modern Art (MoMA)",
              "Indianapolis Museum of Art at Newfields",
              "de la Cruz Collection"
            ],
            "highlights": {
              "partnersConnection": {
                "edges": []
              }
            },
            "auctionResultsConnection": {
              "edges": [
                {
                  "node": {
                    "__typename": "AuctionResult",
                    "id": "QXVjdGlvblJlc3VsdDozMjQ0NDI5",
                    "price_realized": {
                      "display": "£13m"
                    },
                    "organization": "Sotheby's",
                    "sale_date": "2011"
                  }
                }
              ]
            },
            "biographyBlurb": {
              "text": "<p>Salvador Dalí was a leading proponent of <a href=\"/gene/surrealism\">Surrealism<\/a>, the 20-century avant-garde movement that sought to release the creative potential of the unconscious through strange, dream-like imagery. “<a href=\"/gene/surrealism\">Surrealism<\/a> is destructive, but it destroys only what it considers to be shackles limiting our vision,” he said. Dalí is specially credited with the innovation of “paranoia-criticism,” a philosophy of art making he defined as “irrational understanding based on the interpretive-critical association of delirious phenomena.” In addition to meticulously painting fantastic compositions, such as <em>The Accommodations of Desire<\/em> (1929) and the <a href=\"/collection/salvador-dali-melting-clocks\">melting clocks<\/a> in his famed <em>The Persistence of Memory<\/em> (1931), Dalí was a prolific writer and early filmmaker, and cultivated an eccentric public persona with his flamboyant mustache, pet ocelot, and outlandish behavior and quips. <\/p>\n"
            },
            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
            "is_followed": False,
            "related": {
              "artistsConnection": {
                "pageInfo": {
                  "hasNextPage": True,
                  "endCursor": "YXJyYXljb25uZWN0aW9uOjM="
                },
                "edges": [
                  {
                    "node": {
                      "name": "Max Ernst",
                      "slug": "max-ernst",
                      "href": "/artist/max-ernst",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FUUEzIl7siZqz25gXGIFAbA%2Flarge.jpg"
                        }
                      },
                      "formatted_nationality_and_birthday": "German, 1891–1976",
                      "id": "QXJ0aXN0OjRkZTZiNGRlYTllNjg3MDAwMTAwMDc1Zg==",
                      "internalID": "4de6b4dea9e687000100075f",
                      "is_followed": False,
                      "counts": {
                        "follows": 9595
                      },
                      "__typename": "Artist"
                    },
                    "cursor": "YXJyYXljb25uZWN0aW9uOjA="
                  },
                  {
                    "node": {
                      "name": "René Magritte",
                      "slug": "rene-magritte",
                      "href": "/artist/rene-magritte",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FS4YIgw6IeYJjMFuCLJoAVg%2Flarge.jpg"
                        }
                      },
                      "formatted_nationality_and_birthday": "Belgian, 1898–1967",
                      "id": "QXJ0aXN0OjRlOTc0YmFlMDMwNzgwMDAwMTAwMTk2Ng==",
                      "internalID": "4e974bae0307800001001966",
                      "is_followed": False,
                      "counts": {
                        "follows": 13235
                      },
                      "__typename": "Artist"
                    },
                    "cursor": "YXJyYXljb25uZWN0aW9uOjE="
                  },
                  {
                    "node": {
                      "name": "Joan Miró",
                      "slug": "joan-miro",
                      "href": "/artist/joan-miro",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FDvZH9-qtZotZ5w1596tctA%2Flarge.jpg"
                        }
                      },
                      "formatted_nationality_and_birthday": "Spanish, 1893–1983",
                      "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                      "internalID": "4d8b927f4eb68a1b2c00017c",
                      "is_followed": False,
                      "counts": {
                        "follows": 22266
                      },
                      "__typename": "Artist"
                    },
                    "cursor": "YXJyYXljb25uZWN0aW9uOjI="
                  },
                  {
                    "node": {
                      "name": "Eugene Berman",
                      "slug": "eugene-berman",
                      "href": "/artist/eugene-berman",
                      "image": {
                        "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FjG2rr_ZOZczN0UuAhANQPQ%2Flarge.jpg"
                        }
                      },
                      "formatted_nationality_and_birthday": "American, 1899–1972",
                      "id": "QXJ0aXN0OjUyOGU3NDRiMWExZTg2ZDQ4YzAwMDA4ZA==",
                      "internalID": "528e744b1a1e86d48c00008d",
                      "is_followed": False,
                      "counts": {
                        "follows": 338
                      },
                      "__typename": "Artist"
                    },
                    "cursor": "YXJyYXljb25uZWN0aW9uOjM="
                  }
                ]
              }
            }
          },
          "href": "/artwork/salvador-dali-madonne",
          "date": "1957",
          "artist_names": "Salvador Dalí",
          "sale_message": "€5,000 - 7,500",
          "partner": {
            "name": "Dali Paris",
            "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
            "type": "Gallery",
            "profile": {
              "image": {
                "resized": {
                  "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FpJInfgBNj3NB4QK1x_0HHQ%2Fmedium250x165.jpg"
                }
              },
              "id": "UHJvZmlsZTo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzI=",
              "slug": "dali-paris",
              "name": "Dali Paris",
              "internalID": "592ea16eb202a34d9949b732",
              "is_followed": False,
              "icon": {
                "url": "https://d32dm0rphc51dk.cloudfront.net/XOf_yFqYK5o4fj3iDVqWOA/square140.png"
              }
            },
            "initials": "DP",
            "href": "/dali-paris",
            "locations": [
              {
                "city": "Paris",
                "id": "TG9jYXRpb246NTkyZWEzY2Y4YjNiODE2OTkwZTA5ZjY5"
              }
            ],
            "isVerifiedSeller": False,
            "internalID": "592ea16eb202a34d9949b731",
            "slug": "dali-paris",
            "is_default_profile_public": True
          },
          "image_rights": "",
          "is_shareable": True,
          "meta_image": {
            "resized": {
              "width": 640,
              "height": 1031,
              "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=640&height=1031&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FdAMtqpwtIUgN0zlJpjYrmA%2Flarge.jpg"
            }
          },
          "meta": {
            "title": "Salvador Dalí | Madonne (1957) | Available for Sale | Artsy",
            "description": "Available for sale from Dali Paris, Salvador Dalí, Madonne (1957), Lithograph, 64.5 × 41 cm",
            "long_description": "Available for sale from Dali Paris, Salvador Dalí, Madonne (1957), Lithograph, 64.5 × 41 cm"
          },
          "context": None,
          "is_price_hidden": False,
          "is_price_range": True,
          "category": "Drawing, Collage or other Work on Paper",
          "dimensions": {
            "in": "25 2/5 × 16 1/10 in",
            "cm": "64.5 × 41 cm"
          },
          "cultural_maker": None,
          "is_biddable": False,
          "edition_sets": [
            {
              "__typename": "EditionSet",
              "id": "RWRpdGlvblNldDo1ZmM0YWMyOGJhNTQxYTNmMjliOWI4YmE=",
              "internalID": "5fc4ac28ba541a3f29b9b8ba",
              "is_acquireable": False,
              "is_offerable": False,
              "sale_message": "€5,000 - 7,500",
              "dimensions": {
                "in": "25 2/5 × 16 1/10 in",
                "cm": "64.5 × 41 cm"
              },
              "edition_of": "Edition of 233"
            }
          ],
          "sale_artwork": None,
          "title": "Madonne",
          "medium": "Lithograph",
          "edition_of": "Edition of 233",
          "attributionClass": {
            "shortDescription": "This work is part of a limited edition set",
            "id": "QXR0cmlidXRpb25DbGFzczpsaW1pdGVkIGVkaXRpb24="
          },
          "myLotStanding": None,
          "is_for_sale": True,
          "is_inquireable": True,
          "priceIncludesTaxDisplay": "VAT included in price",
          "shippingInfo": "Shipping: €150 within Continental Europe, €250 rest of world",
          "shippingOrigin": "Paris, FR",
          "hasCertificateOfAuthenticity": True,
          "description": None,
          "additional_information": "<p>In 1957, the eminent publisher Joseph Foret came to Salvador Dali with an impressive load of lithographic stones and the idea of creating an extraordinary set of illustrations of the famous book by Miguel Cervantes ‘Don Quichotte’. Dali used an unusual technique, which gained popularity after the book was published. Instead of pencil and paint, Dali used an air gun packed with ink. The gun shot right at the plain lithographic stone giving the basis for Dali’s inspiration. Faithful to his habits, Dalí approached this technique experimentally. For his own ‘Don Quichotte’ he did not hesitate even to dip snails in the color so that they leave traces on the stone. Therefore, the works were created spontaneously, the incipit was given by chance.<\/p>\n<p>Salvador Dalí expressed his surrealist vision of universal poetic and literary themes through his vast repertoire of images, characters, and allegories. In his characters Dalí revealed himself as an indisputable master of graphic arts, always renewing his technique, his drawings, and his colors.<\/p>\n<p>Dali, inspired by the virgin of Raphael, gives birth to his Madonna by small projections of ink and crumpled litho paper, titrated with both hands by the creator.<\/p>\n<p>Reference: “The Official Catalog of the Graphic Works of Salvador Dali” by Albert Field.<br>Ref.57-1- E, pages 123-125. Published by The Salvador Dali Archives.<\/p>\n",
          "series": "Don Quichotte",
          "publisher": None,
          "manufacturer": None,
          "canRequestLotConditionsReport": False,
          "framed": {
            "label": "Framed",
            "details": "Not included"
          },
          "signatureInfo": {
            "label": "Signature",
            "details": "Signed in the plate"
          },
          "conditionDescription": {
            "label": "Condition details",
            "details": "Very good condition"
          },
          "certificateOfAuthenticity": {
            "label": "Certificate of authenticity",
            "details": "Included"
          },
          "mediumType": {
            "__typename": "ArtworkMedium",
            "name": "Drawing, Collage or other Work on Paper",
            "longDescription": "Includes collages; drawings; figure drawing; pen and ink; sketch. This also includes paintings where paper is the support."
          },
          "articles": [],
          "literature": "<p>The Official Catalogue of The Graphic Works of Salvador Dali A.Field 57-1, p. 123<\/p>\n",
          "exhibition_history": None,
          "provenance": None,
          "image_alt": "Salvador Dalí, ‘Madonne’, 1957, Dali Paris",
          "id": "QXJ0d29yazo1ZGM2YTRkNDk2YzQ5MTAwMGU1YmIxNzA=",
          "is_saved": False,
          "images": [
            {
              "url": "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/medium.jpg",
              "internalID": "5dc6a4d5e3a4d9000e11f1b3",
              "uri": "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/large.jpg",
              "placeholder": {
                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=30&height=48&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FdAMtqpwtIUgN0zlJpjYrmA%2Fsmall.jpg"
              },
              "aspectRatio": 0.62,
              "is_zoomable": True,
              "is_default": True,
              "deepZoom": {
                "Image": {
                  "xmlns": "http://schemas.microsoft.com/deepzoom/2008",
                  "Url": "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/",
                  "Format": "jpg",
                  "TileSize": 512,
                  "Overlap": 0,
                  "Size": {
                    "Width": 2500,
                    "Height": 4030
                  }
                }
              }
            }
          ],
          "artworkMeta": {
            "share": "Check out Salvador Dalí, Madonne (1957), From Dali Paris"
          },
          "image": {
            "internalID": "5dc6a4d5e3a4d9000e11f1b3",
            "url": "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/larger.jpg",
            "height": 4030,
            "width": 2500
          },
          "is_downloadable": False,
          "is_hangable": True,
          "contextGrids": [
            {
              "__typename": "ArtistArtworkGrid",
              "title": "Other works by Salvador Dalí",
              "ctaTitle": "View all works by Salvador Dalí",
              "ctaHref": "/artist/salvador-dali",
              "artworksConnection": {
                "edges": [
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZTdlNmRhY2QyYmQ4NDAwMTI0NjRhMDE=",
                      "slug": "salvador-dali-venus-in-the-legs",
                      "href": "/artwork/salvador-dali-venus-in-the-legs",
                      "internalID": "5e7e6dacd2bd840012464a01",
                      "image": {
                        "aspect_ratio": 0.82,
                        "placeholder": "121.39275766016712%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/wcWxq_WX2tWjO9ejZxnA7Q/large.jpg"
                      },
                      "title": "Venus in the Legs",
                      "image_title": "Salvador Dalí, ‘Venus in the Legs’, 1964",
                      "date": "1964",
                      "sale_message": "Contact For Price",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "New River Fine Art",
                        "href": "/new-river-fine-art",
                        "id": "UGFydG5lcjo1OTc2NjIxNDhiM2I4MTFhNzExMzlkOTQ=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZThjZGYxOTk0YzBiMTAwMGQ4YzcwYWM=",
                      "slug": "salvador-dali-trajan-horse-1",
                      "href": "/artwork/salvador-dali-trajan-horse-1",
                      "internalID": "5e8cdf1994c0b1000d8c70ac",
                      "image": {
                        "aspect_ratio": 1.17,
                        "placeholder": "85.16666666666667%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/ZFPyxzkl2NszlHOWdliEEA/large.jpg"
                      },
                      "title": "Trajan Horse",
                      "image_title": "Salvador Dalí, ‘Trajan Horse’, 1981",
                      "date": "1981",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Heritage Auctions",
                        "href": "/auction/partner-595e67cab202a301c4818569",
                        "id": "UGFydG5lcjo1OTVlNjdjYWIyMDJhMzAxYzQ4MTg1Njk=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1ZThjZGMwYTQxMGIxNTAwMTE3MjM2Nzk=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 2
                        },
                        "highest_bid": {
                          "display": "$700"
                        },
                        "opening_bid": {
                          "display": "$650"
                        },
                        "id": "U2FsZUFydHdvcms6NWU4Y2RmMWI5Zjc4YzAwMDEwMWYwNGI3"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZjY2ODNlYmU1ZGViYjAwMTI2ZjU0Y2Y=",
                      "slug": "salvador-dali-mythology-leda-and-swan-leda-et-le-cygne",
                      "href": "/artwork/salvador-dali-mythology-leda-and-swan-leda-et-le-cygne",
                      "internalID": "5f6683ebe5debb00126f54cf",
                      "image": {
                        "aspect_ratio": 0.81,
                        "placeholder": "123.66666666666666%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/R6_-VNUT5fbrXUHJDPD1fQ/large.jpg"
                      },
                      "title": "Mythology: Leda and Swan - Leda Et Le Cygne ",
                      "image_title": "Salvador Dalí, ‘Mythology: Leda and Swan - Leda Et Le Cygne ’, 1963-1965",
                      "date": "1963-1965",
                      "sale_message": "Contact For Price",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Off The Wall Gallery",
                        "href": "/off-the-wall-gallery",
                        "id": "UGFydG5lcjo1OTBjZDlkYTEzOWIyMTIwMzBjYmQ0YjI=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZDVjMjM2NmZhYThkMDAwMTFkMWRlNDE=",
                      "slug": "salvador-dali-the-ballet-of-the-flowers-1",
                      "href": "/artwork/salvador-dali-the-ballet-of-the-flowers-1",
                      "internalID": "5d5c2366faa8d00011d1de41",
                      "image": {
                        "aspect_ratio": 0.76,
                        "placeholder": "131.17621337997377%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/O88NczcNfnBWiqYps8OQOA/large.jpg"
                      },
                      "title": "The Ballet of the Flowers",
                      "image_title": "Salvador Dalí, ‘The Ballet of the Flowers’, 1980",
                      "date": "1980",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Heritage Auctions",
                        "href": "/auction/partner-595e67cab202a301c4818569",
                        "id": "UGFydG5lcjo1OTVlNjdjYWIyMDJhMzAxYzQ4MTg1Njk=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1ZDVjMGZlMTAzZDlkNTAwMTI3ZTZlYjM=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 7
                        },
                        "highest_bid": {
                          "display": "$1,600"
                        },
                        "opening_bid": {
                          "display": "$650"
                        },
                        "id": "U2FsZUFydHdvcms6NWQ1YzIzNjYwM2Q5ZDUwMDEyN2U3MWVk"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZDVjMjM2OGZhYThkMDAwMGRmMGNhMWQ=",
                      "slug": "salvador-dali-dali-dreams-1",
                      "href": "/artwork/salvador-dali-dali-dreams-1",
                      "internalID": "5d5c2368faa8d0000df0ca1d",
                      "image": {
                        "aspect_ratio": 0.72,
                        "placeholder": "138.95321908290876%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/A6kxC0Qupe4fKBfCvtMx7A/large.jpg"
                      },
                      "title": "Dali Dreams",
                      "image_title": "Salvador Dalí, ‘Dali Dreams’, 1978",
                      "date": "1978",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Heritage Auctions",
                        "href": "/auction/partner-595e67cab202a301c4818569",
                        "id": "UGFydG5lcjo1OTVlNjdjYWIyMDJhMzAxYzQ4MTg1Njk=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1ZDVjMGZlMTAzZDlkNTAwMTI3ZTZlYjM=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 3
                        },
                        "highest_bid": {
                          "display": "$800"
                        },
                        "opening_bid": {
                          "display": "$650"
                        },
                        "id": "U2FsZUFydHdvcms6NWQ1YzIzNjkwM2Q5ZDUwMDBlYzM2N2Zj"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZDVjMjM2YjhhOTc4YTAwMTNiZmQ5YzM=",
                      "slug": "salvador-dali-anenome-per-anti-pasti-from-florals",
                      "href": "/artwork/salvador-dali-anenome-per-anti-pasti-from-florals",
                      "internalID": "5d5c236b8a978a0013bfd9c3",
                      "image": {
                        "aspect_ratio": 0.73,
                        "placeholder": "137.29977116704805%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/QKfpwK-U19W75dofj7XwDw/large.jpg"
                      },
                      "title": "Anenome per anti-pasti, from Florals",
                      "image_title": "Salvador Dalí, ‘Anenome per anti-pasti, from Florals’, 1972",
                      "date": "1972",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Heritage Auctions",
                        "href": "/auction/partner-595e67cab202a301c4818569",
                        "id": "UGFydG5lcjo1OTVlNjdjYWIyMDJhMzAxYzQ4MTg1Njk=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1ZDVjMGZlMTAzZDlkNTAwMTI3ZTZlYjM=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 17
                        },
                        "highest_bid": {
                          "display": "$700"
                        },
                        "opening_bid": {
                          "display": "$240"
                        },
                        "id": "U2FsZUFydHdvcms6NWQ1YzIzNmI5Mzg3NDEwMDBlYjFkZGQ5"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YmQzNWQ0MmQ0NzQxMTRiOGJiMTk1MzU=",
                      "slug": "salvador-dali-bande-de-moebius",
                      "href": "/artwork/salvador-dali-bande-de-moebius",
                      "internalID": "5bd35d42d474114b8bb19535",
                      "image": {
                        "aspect_ratio": 0.75,
                        "placeholder": "133.33333333333331%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/1dcDPcLDrgfO01mBL-vcbA/large.jpg"
                      },
                      "title": "Bande de Moëbius",
                      "image_title": "Salvador Dalí, ‘Bande de Moëbius’, 1970",
                      "date": "1970",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Capsule Gallery Auction",
                        "href": "/auction/capsule-gallery-auction",
                        "id": "UGFydG5lcjo1YWUxNmUwYTljMThkYjRjMTc3YzZhN2M=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1YmQzM2QwZTM0NDc4NjE4ZjA1MTQ4YjY=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 2
                        },
                        "highest_bid": {
                          "display": "$750"
                        },
                        "opening_bid": {
                          "display": "$700"
                        },
                        "id": "U2FsZUFydHdvcms6NWJkMzVkNDRjMjc1MWExZjA2NjI3ZjE2"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1OTU2OWU3YWEwOWE2NzVhZTUyM2VkYTc=",
                      "slug": "salvador-dali-hippies-suite-femmes-fleurs-au-piano",
                      "href": "/artwork/salvador-dali-hippies-suite-femmes-fleurs-au-piano",
                      "internalID": "59569e7aa09a675ae523eda7",
                      "image": {
                        "aspect_ratio": 0.82,
                        "placeholder": "121.97957027122226%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/CchA583uR2qS2hBC-Atjdw/large.jpg"
                      },
                      "title": "Hippies Suite: Femmes Fleurs Au Piano ",
                      "image_title": "Salvador Dalí, ‘Hippies Suite: Femmes Fleurs Au Piano ’, 1973",
                      "date": "1973",
                      "sale_message": "Contact For Price",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Off The Wall Gallery",
                        "href": "/off-the-wall-gallery",
                        "id": "UGFydG5lcjo1OTBjZDlkYTEzOWIyMTIwMzBjYmQ0YjI=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  }
                ]
              }
            },
            {
              "__typename": "PartnerArtworkGrid",
              "title": "Other works from Dali Paris",
              "ctaTitle": "View all works from Dali Paris",
              "ctaHref": "/dali-paris",
              "artworksConnection": {
                "edges": [
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo2MDA4NDQ2MTg1YmRiYTU0YmI0YzQzMTM=",
                      "slug": "salvador-dali-isis-porte-portrait",
                      "href": "/artwork/salvador-dali-isis-porte-portrait",
                      "internalID": "6008446185bdba54bb4c4313",
                      "image": {
                        "aspect_ratio": 0.75,
                        "placeholder": "133.33333333333331%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/hk5-f0dhEOLgyC3TGmbygQ/large.jpg"
                      },
                      "title": "Isis Porte portrait",
                      "image_title": "Salvador Dalí, ‘Isis Porte portrait’, 1967",
                      "date": "1967",
                      "sale_message": "€80,000 - 130,000",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Dali Paris",
                        "href": "/dali-paris",
                        "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo2MDA2YTNkZDZhMDI0OTIxZWJjYmE3M2E=",
                      "slug": "salvador-dali-down-the-rabbit-hole-1",
                      "href": "/artwork/salvador-dali-down-the-rabbit-hole-1",
                      "internalID": "6006a3dd6a024921ebcba73a",
                      "image": {
                        "aspect_ratio": 0.68,
                        "placeholder": "147.54098360655738%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/GizR4ZGOQUr3iQHDSy25YQ/large.jpg"
                      },
                      "title": "Down the rabbit hole",
                      "image_title": "Salvador Dalí, ‘Down the rabbit hole’, 1969",
                      "date": "1969",
                      "sale_message": "€2,500 - 5,000",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Dali Paris",
                        "href": "/dali-paris",
                        "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZjdmMWEyODM0YjY5MTAwMGU3ZTYwZmY=",
                      "slug": "salvador-dali-chinese-roquin",
                      "href": "/artwork/salvador-dali-chinese-roquin",
                      "internalID": "5f7f1a2834b691000e7e60ff",
                      "image": {
                        "aspect_ratio": 0.71,
                        "placeholder": "141.47027787548365%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/JBR7r726XJxG46C2YIa99w/large.jpg"
                      },
                      "title": "Chinese Roquin",
                      "image_title": "Salvador Dalí, ‘Chinese Roquin’, 1973",
                      "date": "1973",
                      "sale_message": "€2,500 - 5,000",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Dali Paris",
                        "href": "/dali-paris",
                        "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZjdlZWFkM2YxNjE0YjAwMGRmNGRmNjk=",
                      "slug": "salvador-dali-leg-tribute-ceremonial",
                      "href": "/artwork/salvador-dali-leg-tribute-ceremonial",
                      "internalID": "5f7eead3f1614b000df4df69",
                      "image": {
                        "aspect_ratio": 0.69,
                        "placeholder": "144.04934687953556%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/6LtY0VCqQtGiyVv0pR069w/large.jpg"
                      },
                      "title": "Leg Tribute Ceremonial",
                      "image_title": "Salvador Dalí, ‘Leg Tribute Ceremonial’, 1973",
                      "date": "1973",
                      "sale_message": "€2,500 - 5,000",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Dali Paris",
                        "href": "/dali-paris",
                        "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZjZmMTViODViMmQ2MDAwMGUxMWMwZDU=",
                      "slug": "salvador-dali-familiar-phallus",
                      "href": "/artwork/salvador-dali-familiar-phallus",
                      "internalID": "5f6f15b85b2d60000e11c0d5",
                      "image": {
                        "aspect_ratio": 0.69,
                        "placeholder": "143.89285714285714%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/Xdme27n_bOge93qS974V0w/large.jpg"
                      },
                      "title": "Familiar Phallus",
                      "image_title": "Salvador Dalí, ‘Familiar Phallus’, 1973",
                      "date": "1973",
                      "sale_message": "€2,500 - 5,000",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Dali Paris",
                        "href": "/dali-paris",
                        "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZjZmMTM2ODgwZmNkNzAwMGRjZDE4Nzg=",
                      "slug": "salvador-dali-giant-pastry-cook",
                      "href": "/artwork/salvador-dali-giant-pastry-cook",
                      "internalID": "5f6f136880fcd7000dcd1878",
                      "image": {
                        "aspect_ratio": 0.7,
                        "placeholder": "143.2442328817283%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/H4Q9pEzdntUWtyS2w-JFUw/large.jpg"
                      },
                      "title": "Giant Pastry Cook",
                      "image_title": "Salvador Dalí, ‘Giant Pastry Cook’, 1973",
                      "date": "1973",
                      "sale_message": "€2,500 - 5,000",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Dali Paris",
                        "href": "/dali-paris",
                        "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZjY3MjgyNzI0Mzg3MTAwMGVhM2EzMDQ=",
                      "slug": "salvador-dali-faith-moves-mountains",
                      "href": "/artwork/salvador-dali-faith-moves-mountains",
                      "internalID": "5f672827243871000ea3a304",
                      "image": {
                        "aspect_ratio": 0.73,
                        "placeholder": "136.58854166666669%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/jWwejI8rFSIwAW2WxkOq1A/large.jpg"
                      },
                      "title": "Faith Moves Mountains",
                      "image_title": "Salvador Dalí, ‘Faith Moves Mountains’, 1959",
                      "date": "1959",
                      "sale_message": "€1,000 - 2,500",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Dali Paris",
                        "href": "/dali-paris",
                        "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZjQ5MGMyN2JjNzFiODAwMGZkNTM5MTA=",
                      "slug": "salvador-dali-bell-figure",
                      "href": "/artwork/salvador-dali-bell-figure",
                      "internalID": "5f490c27bc71b8000fd53910",
                      "image": {
                        "aspect_ratio": 0.71,
                        "placeholder": "140.76704545454547%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/2ZxTfbmthsGkr126SyFDtw/large.jpg"
                      },
                      "title": "Bell Figure",
                      "image_title": "Salvador Dalí, ‘Bell Figure’, 1973",
                      "date": "1973",
                      "sale_message": "€2,500 - 5,000",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg==",
                          "href": "/artist/salvador-dali",
                          "name": "Salvador Dalí"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Dali Paris",
                        "href": "/dali-paris",
                        "id": "UGFydG5lcjo1OTJlYTE2ZWIyMDJhMzRkOTk0OWI3MzE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  }
                ]
              }
            },
            {
              "__typename": "RelatedArtworkGrid",
              "title": "Related works",
              "ctaTitle": None,
              "ctaHref": None,
              "artworksConnection": {
                "edges": [
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YjdmZDQxZWYzNDc0NTBiNjQ1N2UzMDI=",
                      "slug": "joan-miro-les-essencies-de-la-terra-14",
                      "href": "/artwork/joan-miro-les-essencies-de-la-terra-14",
                      "internalID": "5b7fd41ef347450b6457e302",
                      "image": {
                        "aspect_ratio": 1.45,
                        "placeholder": "69.04296875%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/wqPwOfJoTo-b1zFpRxnczA/large.jpg"
                      },
                      "title": "Les Essències de la Terra",
                      "image_title": "Joan Miró, ‘Les Essències de la Terra’, 1968",
                      "date": "1968",
                      "sale_message": "€650",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                          "href": "/artist/joan-miro",
                          "name": "Joan Miró"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Wallector",
                        "href": "/wallector",
                        "id": "UGFydG5lcjo1OTU2Njk5ZDJhODkzYTZiNDYwNjk0ZDM=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1ZWRlMjQ5ODM1YzQ0NzAwMTJlODg2NTg=",
                      "slug": "pablo-picasso-profils-et-tetes",
                      "href": "/artwork/pablo-picasso-profils-et-tetes",
                      "internalID": "5ede249835c4470012e88658",
                      "image": {
                        "aspect_ratio": 1.5,
                        "placeholder": "66.66666666666666%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/Y1NlSs2GNBqE9Or7AYfxCw/large.jpg"
                      },
                      "title": "Profils et Têtes",
                      "image_title": "Pablo Picasso, ‘Profils et Têtes’, 1967",
                      "date": "1967",
                      "sale_message": "Contact For Price",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkOGI5MjhiNGViNjhhMWIyYzAwMDFmMg==",
                          "href": "/artist/pablo-picasso",
                          "name": "Pablo Picasso"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Piano Nobile",
                        "href": "/piano-nobile",
                        "id": "UGFydG5lcjo1NTMwNDBlZDc3NmY3MjM2MDM2NTAzMDA=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YTdhMWFkYzhiMGMxNDA5NjQ4NmZlYTg=",
                      "slug": "after-joan-miro-atelier-mourlot-1967",
                      "href": "/artwork/after-joan-miro-atelier-mourlot-1967",
                      "internalID": "5a7a1adc8b0c14096486fea8",
                      "image": {
                        "aspect_ratio": 0.71,
                        "placeholder": "141.227125941873%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/BIV8j709eB78h6u0Yf6nlg/large.jpg"
                      },
                      "title": "Atelier Mourlot, 1967",
                      "image_title": "Joan Miró, ‘Atelier Mourlot, 1967’, 1967",
                      "date": "1967",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                          "href": "/artist/joan-miro",
                          "name": "Joan Miró"
                        },
                        {
                          "id": "QXJ0aXN0OjRkZGU3MGExMzA2ZjY4MDAwMTAwMzZlZg==",
                          "href": "/artist/alexander-calder",
                          "name": "Alexander Calder"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Forum Auctions",
                        "href": "/auction/forum-auctions",
                        "id": "UGFydG5lcjo1OTVlNjdhNWM5ZGMyNDFiZThjYjQyNDU=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1YTdhMTgwODc2MjJkZDQ5ZDZkYzQ5MTY=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 0
                        },
                        "highest_bid": {
                          "display": None
                        },
                        "opening_bid": {
                          "display": "£180"
                        },
                        "id": "U2FsZUFydHdvcms6NWE3YTFhZGVjZDUzMGU0OGQ5NDk2Nzgy"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YWY1ZjZiZmNiNGMyNzU5ZTI5NjI3YzY=",
                      "slug": "eduardo-chillida-untitled-2-1",
                      "href": "/artwork/eduardo-chillida-untitled-2-1",
                      "internalID": "5af5f6bfcb4c2759e29627c6",
                      "image": {
                        "aspect_ratio": 1.21,
                        "placeholder": "82.6%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/7ZWbJOz3-xVf8WKfrtlwPg/large.jpg"
                      },
                      "title": "Untitled 2",
                      "image_title": "Eduardo Chillida, ‘Untitled 2’, 1961",
                      "date": "1961",
                      "sale_message": "Sold",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRlOTczNWRkN2QxNDJjMDAwMTAwMGYzYw==",
                          "href": "/artist/eduardo-chillida",
                          "name": "Eduardo Chillida"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Baterbys",
                        "href": "/baterbys",
                        "id": "UGFydG5lcjo1OGVkNDg5ZGM5ZGMyNDIzOTcxMjY3NTQ=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YTNlYzMyNzljMThkYjAyZTU5ZWIwNTQ=",
                      "slug": "joan-miro-les-guetteurs-the-watchers-and-batteuse-paysage-champagne",
                      "href": "/artwork/joan-miro-les-guetteurs-the-watchers-and-batteuse-paysage-champagne",
                      "internalID": "5a3ec3279c18db02e59eb054",
                      "image": {
                        "aspect_ratio": 0.69,
                        "placeholder": "144.39655172413794%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/_SFek7sm7wdF7AhRyISwgg/large.jpg"
                      },
                      "title": "Les Guetteurs (The Watchers); and Batteuse Paysage Champagne",
                      "image_title": "Joan Miró, ‘Les Guetteurs (The Watchers); and Batteuse Paysage Champagne’, 1964; and 1954",
                      "date": "1964; and 1954",
                      "sale_message": None,
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                          "href": "/artist/joan-miro",
                          "name": "Joan Miró"
                        },
                        {
                          "id": "QXJ0aXN0OjRlOTU5Yjc4Yzg4OTA4MDAwMTAwNjI5Zg==",
                          "href": "/artist/raoul-dufy",
                          "name": "Raoul Dufy"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Phillips",
                        "href": "/auction/phillips-1",
                        "id": "UGFydG5lcjo1OTVlNjhhNmIyMDJhMzAxYzQ4MTg1OGQ=",
                        "type": "Auction House"
                      },
                      "sale": {
                        "is_auction": True,
                        "is_closed": True,
                        "id": "U2FsZTo1YTM4NDE0Y2M5ZGMyNDVjMmI1ZTA2OTI=",
                        "is_live_open": False,
                        "is_open": False,
                        "is_preview": False,
                        "display_timely_at": None
                      },
                      "sale_artwork": {
                        "counts": {
                          "bidder_positions": 2
                        },
                        "highest_bid": {
                          "display": "£1,300"
                        },
                        "opening_bid": {
                          "display": "£1,200"
                        },
                        "id": "U2FsZUFydHdvcms6NWEzZWMzMjcyYTg5M2EwNWQ3Y2I1MGNk"
                      },
                      "is_inquireable": False,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1YTc5YjgwOTc2MjJkZDQ4Y2RiZDY4YTA=",
                      "slug": "antoni-tapies-trois-gris-et-marron",
                      "href": "/artwork/antoni-tapies-trois-gris-et-marron",
                      "internalID": "5a79b8097622dd48cdbd68a0",
                      "image": {
                        "aspect_ratio": 0.71,
                        "placeholder": "141.12458654906283%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/8JPbx4e0QwmOkywQbKmaUw/large.jpg"
                      },
                      "title": "Trois Gris Et Marron",
                      "image_title": "Antoni Tàpies, ‘Trois Gris Et Marron’, 1967",
                      "date": "1967",
                      "sale_message": "Under €4,850",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRkYzk5MmEyOTk3NDQ2MDAwMTAwMzhiOQ==",
                          "href": "/artist/antoni-tapies",
                          "name": "Antoni Tàpies"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Kunzt Gallery",
                        "href": "/kunzt-gallery",
                        "id": "UGFydG5lcjo1OWY0OTVkYzhiMGMxNDMzMzVmNjkwNmE=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1Zjk4MmU2MjM2ZjA4MDAwMGU4YjQ3OGI=",
                      "slug": "manolo-millares-pintura-1",
                      "href": "/artwork/manolo-millares-pintura-1",
                      "internalID": "5f982e6236f080000e8b478b",
                      "image": {
                        "aspect_ratio": 1.33,
                        "placeholder": "75%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/hjTexVnxDkNkANPdV2wTjg/large.jpg"
                      },
                      "title": "Pintura",
                      "image_title": "Manolo Millares, ‘Pintura’, 1967",
                      "date": "1967",
                      "sale_message": "Contact For Price",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjUwNmIzM2RkNDQ2NjE3MDAwMjAwMTNhMg==",
                          "href": "/artist/manolo-millares",
                          "name": "Manolo Millares"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Artelandia Gallery",
                        "href": "/artelandia-gallery",
                        "id": "UGFydG5lcjo1Zjk2YWY3NjMxODdiMDAwMTEyZmJmYTg=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  },
                  {
                    "__typename": "ArtworkEdge",
                    "node": {
                      "id": "QXJ0d29yazo1NzhmNGE3NjEzOWIyMTMxN2UwMDUwOTY=",
                      "slug": "wifredo-lam-untitled-20",
                      "href": "/artwork/wifredo-lam-untitled-20",
                      "internalID": "578f4a76139b21317e005096",
                      "image": {
                        "aspect_ratio": 0.78,
                        "placeholder": "128.21659215101838%",
                        "url": "https://d32dm0rphc51dk.cloudfront.net/JfrTO8a6ScSPEXAFQC3j1w/large.jpg"
                      },
                      "title": "Untitled ",
                      "image_title": "Wifredo Lam, ‘Untitled ’, 1946",
                      "date": "1946",
                      "sale_message": "Sold",
                      "cultural_maker": None,
                      "artists": [
                        {
                          "id": "QXJ0aXN0OjRlOTc0NzdmNmJhNzEyMDAwMTAwMTY1MA==",
                          "href": "/artist/wifredo-lam",
                          "name": "Wifredo Lam"
                        }
                      ],
                      "collecting_institution": None,
                      "partner": {
                        "name": "Galerie F. Hessler",
                        "href": "/galerie-f-hessler",
                        "id": "UGFydG5lcjo1NmJhMTY5YzY2ZmQxYzY3MGIwMDAwNmQ=",
                        "type": "Gallery"
                      },
                      "sale": None,
                      "sale_artwork": None,
                      "is_inquireable": True,
                      "is_saved": False,
                      "is_biddable": False
                    }
                  }
                ]
              }
            }
          ],
          "layers": [
            {
              "name": "Most Similar",
              "internalID": "main",
              "id": "QXJ0d29ya0xheWVyOm1haW4="
            },
            {
              "name": "For Sale",
              "internalID": "for-sale",
              "id": "QXJ0d29ya0xheWVyOmZvci1zYWxl"
            }
          ],
          "layer": {
            "name": "Most Similar",
            "artworksConnection": {
              "edges": [
                {
                  "__typename": "ArtworkEdge",
                  "node": {
                    "id": "QXJ0d29yazo1YjdmZDQxZWYzNDc0NTBiNjQ1N2UzMDI=",
                    "slug": "joan-miro-les-essencies-de-la-terra-14",
                    "href": "/artwork/joan-miro-les-essencies-de-la-terra-14",
                    "internalID": "5b7fd41ef347450b6457e302",
                    "image": {
                      "aspect_ratio": 1.45,
                      "placeholder": "69.04296875%",
                      "url": "https://d32dm0rphc51dk.cloudfront.net/wqPwOfJoTo-b1zFpRxnczA/large.jpg"
                    },
                    "title": "Les Essències de la Terra",
                    "image_title": "Joan Miró, ‘Les Essències de la Terra’, 1968",
                    "date": "1968",
                    "sale_message": "€650",
                    "cultural_maker": None,
                    "artists": [
                      {
                        "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                        "href": "/artist/joan-miro",
                        "name": "Joan Miró"
                      }
                    ],
                    "collecting_institution": None,
                    "partner": {
                      "name": "Wallector",
                      "href": "/wallector",
                      "id": "UGFydG5lcjo1OTU2Njk5ZDJhODkzYTZiNDYwNjk0ZDM=",
                      "type": "Gallery"
                    },
                    "sale": None,
                    "sale_artwork": None,
                    "is_inquireable": True,
                    "is_saved": False,
                    "is_biddable": False
                  }
                },
                {
                  "__typename": "ArtworkEdge",
                  "node": {
                    "id": "QXJ0d29yazo1ZWRlMjQ5ODM1YzQ0NzAwMTJlODg2NTg=",
                    "slug": "pablo-picasso-profils-et-tetes",
                    "href": "/artwork/pablo-picasso-profils-et-tetes",
                    "internalID": "5ede249835c4470012e88658",
                    "image": {
                      "aspect_ratio": 1.5,
                      "placeholder": "66.66666666666666%",
                      "url": "https://d32dm0rphc51dk.cloudfront.net/Y1NlSs2GNBqE9Or7AYfxCw/large.jpg"
                    },
                    "title": "Profils et Têtes",
                    "image_title": "Pablo Picasso, ‘Profils et Têtes’, 1967",
                    "date": "1967",
                    "sale_message": "Contact For Price",
                    "cultural_maker": None,
                    "artists": [
                      {
                        "id": "QXJ0aXN0OjRkOGI5MjhiNGViNjhhMWIyYzAwMDFmMg==",
                        "href": "/artist/pablo-picasso",
                        "name": "Pablo Picasso"
                      }
                    ],
                    "collecting_institution": None,
                    "partner": {
                      "name": "Piano Nobile",
                      "href": "/piano-nobile",
                      "id": "UGFydG5lcjo1NTMwNDBlZDc3NmY3MjM2MDM2NTAzMDA=",
                      "type": "Gallery"
                    },
                    "sale": None,
                    "sale_artwork": None,
                    "is_inquireable": True,
                    "is_saved": False,
                    "is_biddable": False
                  }
                },
                {
                  "__typename": "ArtworkEdge",
                  "node": {
                    "id": "QXJ0d29yazo1YTdhMWFkYzhiMGMxNDA5NjQ4NmZlYTg=",
                    "slug": "after-joan-miro-atelier-mourlot-1967",
                    "href": "/artwork/after-joan-miro-atelier-mourlot-1967",
                    "internalID": "5a7a1adc8b0c14096486fea8",
                    "image": {
                      "aspect_ratio": 0.71,
                      "placeholder": "141.227125941873%",
                      "url": "https://d32dm0rphc51dk.cloudfront.net/BIV8j709eB78h6u0Yf6nlg/large.jpg"
                    },
                    "title": "Atelier Mourlot, 1967",
                    "image_title": "Joan Miró, ‘Atelier Mourlot, 1967’, 1967",
                    "date": "1967",
                    "sale_message": None,
                    "cultural_maker": None,
                    "artists": [
                      {
                        "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                        "href": "/artist/joan-miro",
                        "name": "Joan Miró"
                      },
                      {
                        "id": "QXJ0aXN0OjRkZGU3MGExMzA2ZjY4MDAwMTAwMzZlZg==",
                        "href": "/artist/alexander-calder",
                        "name": "Alexander Calder"
                      }
                    ],
                    "collecting_institution": None,
                    "partner": {
                      "name": "Forum Auctions",
                      "href": "/auction/forum-auctions",
                      "id": "UGFydG5lcjo1OTVlNjdhNWM5ZGMyNDFiZThjYjQyNDU=",
                      "type": "Auction House"
                    },
                    "sale": {
                      "is_auction": True,
                      "is_closed": True,
                      "id": "U2FsZTo1YTdhMTgwODc2MjJkZDQ5ZDZkYzQ5MTY=",
                      "is_live_open": False,
                      "is_open": False,
                      "is_preview": False,
                      "display_timely_at": None
                    },
                    "sale_artwork": {
                      "counts": {
                        "bidder_positions": 0
                      },
                      "highest_bid": {
                        "display": None
                      },
                      "opening_bid": {
                        "display": "£180"
                      },
                      "id": "U2FsZUFydHdvcms6NWE3YTFhZGVjZDUzMGU0OGQ5NDk2Nzgy"
                    },
                    "is_inquireable": False,
                    "is_saved": False,
                    "is_biddable": False
                  }
                },
                {
                  "__typename": "ArtworkEdge",
                  "node": {
                    "id": "QXJ0d29yazo1YWY1ZjZiZmNiNGMyNzU5ZTI5NjI3YzY=",
                    "slug": "eduardo-chillida-untitled-2-1",
                    "href": "/artwork/eduardo-chillida-untitled-2-1",
                    "internalID": "5af5f6bfcb4c2759e29627c6",
                    "image": {
                      "aspect_ratio": 1.21,
                      "placeholder": "82.6%",
                      "url": "https://d32dm0rphc51dk.cloudfront.net/7ZWbJOz3-xVf8WKfrtlwPg/large.jpg"
                    },
                    "title": "Untitled 2",
                    "image_title": "Eduardo Chillida, ‘Untitled 2’, 1961",
                    "date": "1961",
                    "sale_message": "Sold",
                    "cultural_maker": None,
                    "artists": [
                      {
                        "id": "QXJ0aXN0OjRlOTczNWRkN2QxNDJjMDAwMTAwMGYzYw==",
                        "href": "/artist/eduardo-chillida",
                        "name": "Eduardo Chillida"
                      }
                    ],
                    "collecting_institution": None,
                    "partner": {
                      "name": "Baterbys",
                      "href": "/baterbys",
                      "id": "UGFydG5lcjo1OGVkNDg5ZGM5ZGMyNDIzOTcxMjY3NTQ=",
                      "type": "Gallery"
                    },
                    "sale": None,
                    "sale_artwork": None,
                    "is_inquireable": True,
                    "is_saved": False,
                    "is_biddable": False
                  }
                },
                {
                  "__typename": "ArtworkEdge",
                  "node": {
                    "id": "QXJ0d29yazo1YTNlYzMyNzljMThkYjAyZTU5ZWIwNTQ=",
                    "slug": "joan-miro-les-guetteurs-the-watchers-and-batteuse-paysage-champagne",
                    "href": "/artwork/joan-miro-les-guetteurs-the-watchers-and-batteuse-paysage-champagne",
                    "internalID": "5a3ec3279c18db02e59eb054",
                    "image": {
                      "aspect_ratio": 0.69,
                      "placeholder": "144.39655172413794%",
                      "url": "https://d32dm0rphc51dk.cloudfront.net/_SFek7sm7wdF7AhRyISwgg/large.jpg"
                    },
                    "title": "Les Guetteurs (The Watchers); and Batteuse Paysage Champagne",
                    "image_title": "Joan Miró, ‘Les Guetteurs (The Watchers); and Batteuse Paysage Champagne’, 1964; and 1954",
                    "date": "1964; and 1954",
                    "sale_message": None,
                    "cultural_maker": None,
                    "artists": [
                      {
                        "id": "QXJ0aXN0OjRkOGI5MjdmNGViNjhhMWIyYzAwMDE3Yw==",
                        "href": "/artist/joan-miro",
                        "name": "Joan Miró"
                      },
                      {
                        "id": "QXJ0aXN0OjRlOTU5Yjc4Yzg4OTA4MDAwMTAwNjI5Zg==",
                        "href": "/artist/raoul-dufy",
                        "name": "Raoul Dufy"
                      }
                    ],
                    "collecting_institution": None,
                    "partner": {
                      "name": "Phillips",
                      "href": "/auction/phillips-1",
                      "id": "UGFydG5lcjo1OTVlNjhhNmIyMDJhMzAxYzQ4MTg1OGQ=",
                      "type": "Auction House"
                    },
                    "sale": {
                      "is_auction": True,
                      "is_closed": True,
                      "id": "U2FsZTo1YTM4NDE0Y2M5ZGMyNDVjMmI1ZTA2OTI=",
                      "is_live_open": False,
                      "is_open": False,
                      "is_preview": False,
                      "display_timely_at": None
                    },
                    "sale_artwork": {
                      "counts": {
                        "bidder_positions": 2
                      },
                      "highest_bid": {
                        "display": "£1,300"
                      },
                      "opening_bid": {
                        "display": "£1,200"
                      },
                      "id": "U2FsZUFydHdvcms6NWEzZWMzMjcyYTg5M2EwNWQ3Y2I1MGNk"
                    },
                    "is_inquireable": False,
                    "is_saved": False,
                    "is_biddable": False
                  }
                },
                {
                  "__typename": "ArtworkEdge",
                  "node": {
                    "id": "QXJ0d29yazo1YTc5YjgwOTc2MjJkZDQ4Y2RiZDY4YTA=",
                    "slug": "antoni-tapies-trois-gris-et-marron",
                    "href": "/artwork/antoni-tapies-trois-gris-et-marron",
                    "internalID": "5a79b8097622dd48cdbd68a0",
                    "image": {
                      "aspect_ratio": 0.71,
                      "placeholder": "141.12458654906283%",
                      "url": "https://d32dm0rphc51dk.cloudfront.net/8JPbx4e0QwmOkywQbKmaUw/large.jpg"
                    },
                    "title": "Trois Gris Et Marron",
                    "image_title": "Antoni Tàpies, ‘Trois Gris Et Marron’, 1967",
                    "date": "1967",
                    "sale_message": "Under €4,850",
                    "cultural_maker": None,
                    "artists": [
                      {
                        "id": "QXJ0aXN0OjRkYzk5MmEyOTk3NDQ2MDAwMTAwMzhiOQ==",
                        "href": "/artist/antoni-tapies",
                        "name": "Antoni Tàpies"
                      }
                    ],
                    "collecting_institution": None,
                    "partner": {
                      "name": "Kunzt Gallery",
                      "href": "/kunzt-gallery",
                      "id": "UGFydG5lcjo1OWY0OTVkYzhiMGMxNDMzMzVmNjkwNmE=",
                      "type": "Gallery"
                    },
                    "sale": None,
                    "sale_artwork": None,
                    "is_inquireable": True,
                    "is_saved": False,
                    "is_biddable": False
                  }
                },
                {
                  "__typename": "ArtworkEdge",
                  "node": {
                    "id": "QXJ0d29yazo1Zjk4MmU2MjM2ZjA4MDAwMGU4YjQ3OGI=",
                    "slug": "manolo-millares-pintura-1",
                    "href": "/artwork/manolo-millares-pintura-1",
                    "internalID": "5f982e6236f080000e8b478b",
                    "image": {
                      "aspect_ratio": 1.33,
                      "placeholder": "75%",
                      "url": "https://d32dm0rphc51dk.cloudfront.net/hjTexVnxDkNkANPdV2wTjg/large.jpg"
                    },
                    "title": "Pintura",
                    "image_title": "Manolo Millares, ‘Pintura’, 1967",
                    "date": "1967",
                    "sale_message": "Contact For Price",
                    "cultural_maker": None,
                    "artists": [
                      {
                        "id": "QXJ0aXN0OjUwNmIzM2RkNDQ2NjE3MDAwMjAwMTNhMg==",
                        "href": "/artist/manolo-millares",
                        "name": "Manolo Millares"
                      }
                    ],
                    "collecting_institution": None,
                    "partner": {
                      "name": "Artelandia Gallery",
                      "href": "/artelandia-gallery",
                      "id": "UGFydG5lcjo1Zjk2YWY3NjMxODdiMDAwMTEyZmJmYTg=",
                      "type": "Gallery"
                    },
                    "sale": None,
                    "sale_artwork": None,
                    "is_inquireable": True,
                    "is_saved": False,
                    "is_biddable": False
                  }
                },
                {
                  "__typename": "ArtworkEdge",
                  "node": {
                    "id": "QXJ0d29yazo1NzhmNGE3NjEzOWIyMTMxN2UwMDUwOTY=",
                    "slug": "wifredo-lam-untitled-20",
                    "href": "/artwork/wifredo-lam-untitled-20",
                    "internalID": "578f4a76139b21317e005096",
                    "image": {
                      "aspect_ratio": 0.78,
                      "placeholder": "128.21659215101838%",
                      "url": "https://d32dm0rphc51dk.cloudfront.net/JfrTO8a6ScSPEXAFQC3j1w/large.jpg"
                    },
                    "title": "Untitled ",
                    "image_title": "Wifredo Lam, ‘Untitled ’, 1946",
                    "date": "1946",
                    "sale_message": "Sold",
                    "cultural_maker": None,
                    "artists": [
                      {
                        "id": "QXJ0aXN0OjRlOTc0NzdmNmJhNzEyMDAwMTAwMTY1MA==",
                        "href": "/artist/wifredo-lam",
                        "name": "Wifredo Lam"
                      }
                    ],
                    "collecting_institution": None,
                    "partner": {
                      "name": "Galerie F. Hessler",
                      "href": "/galerie-f-hessler",
                      "id": "UGFydG5lcjo1NmJhMTY5YzY2ZmQxYzY3MGIwMDAwNmQ=",
                      "type": "Gallery"
                    },
                    "sale": None,
                    "sale_artwork": None,
                    "is_inquireable": True,
                    "is_saved": False,
                    "is_biddable": False
                  }
                }
              ]
            },
            "id": "QXJ0d29ya0xheWVyOm1haW4="
          },
          "artistSeriesConnection": {
            "edges": []
          },
          "seriesArtist": {
            "artistSeriesConnection": {
              "edges": [
                {
                  "node": {
                    "internalID": "0d38ea83-2e16-4846-ac76-7e6a96b723b6",
                    "title": "The Divine Comedy",
                    "slug": "salvador-dali-the-divine-comedy",
                    "featured": False,
                    "artworksCountMessage": "373 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FGGZPqjDTpQGur2lsqFeUww%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "f980c925-3f4c-4d26-af45-ba0f2ae5fa22",
                    "title": "Don Quixote",
                    "slug": "salvador-dali-don-quixote",
                    "featured": False,
                    "artworksCountMessage": "46 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FE1Ulk9KJ0iQIRZDlyehbEw%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "67b5a464-51a3-419b-87d1-b788313cacd4",
                    "title": "Venus",
                    "slug": "salvador-dali-venus",
                    "featured": False,
                    "artworksCountMessage": "40 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FwcWxq_WX2tWjO9ejZxnA7Q%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "c1da431c-426f-4e95-ac86-b8ec064a653b",
                    "title": "The Bible",
                    "slug": "salvador-dali-the-bible",
                    "featured": False,
                    "artworksCountMessage": "38 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FEprKIL3UATLdoMD4ea6XMg%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "5cae3bd1-1516-4481-84f2-6e81c17cf3b9",
                    "title": "Dante",
                    "slug": "salvador-dali-dante",
                    "featured": False,
                    "artworksCountMessage": "37 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FlglZ8nT2AYzDwwVW_JVj2g%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "2f1828bc-90be-4b49-8b65-4f82427ca905",
                    "title": "Mythologies",
                    "slug": "salvador-dali-mythologies",
                    "featured": False,
                    "artworksCountMessage": "31 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F8iNBtjqbTL-WKRzvZYuKCg%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "7bd85620-eafc-4d97-9ad0-231835704199",
                    "title": "Fruits",
                    "slug": "salvador-dali-fruits",
                    "featured": False,
                    "artworksCountMessage": "29 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FQKfpwK-U19W75dofj7XwDw%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "0eb82c98-6a9d-4b32-a20e-8918e1338ff6",
                    "title": "Signs of the Zodiac",
                    "slug": "salvador-dali-signs-of-the-zodiac",
                    "featured": False,
                    "artworksCountMessage": "24 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fb1cKQL8IvN3yIT5fFQtE5Q%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "9a675bdb-0ea4-4be0-a720-f7d37a9ad4ca",
                    "title": "Faust",
                    "slug": "salvador-dali-faust",
                    "featured": False,
                    "artworksCountMessage": "23 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FMJqf4fQIo3skVUYi0W_2pw%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "08994a70-aeb1-4d00-8f14-7345735dd0f7",
                    "title": "Melting Clocks",
                    "slug": "salvador-dali-melting-clocks",
                    "featured": False,
                    "artworksCountMessage": "21 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FCJ-ZqbPozMkY4bQTuj5tuQ%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "6ca2b8ff-99cd-464a-b003-315667dd254a",
                    "title": "Elephants",
                    "slug": "salvador-dali-elephants",
                    "featured": False,
                    "artworksCountMessage": "18 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FWRWLhRJzxS0RYPEc4NsY4g%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "899af2f6-bd5b-4721-a6fd-32767b10a5b9",
                    "title": "Les Amours de Cassandre",
                    "slug": "salvador-dali-les-amours-de-cassandre",
                    "featured": False,
                    "artworksCountMessage": "15 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FmGl0zjCljOVEcxBr_h3POA%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "8e7668a0-10dd-4a8d-93ea-72413cb08297",
                    "title": "Shakespeare",
                    "slug": "salvador-dali-shakespeare",
                    "featured": False,
                    "artworksCountMessage": "14 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F8jZnKiSRgw0zyAPp0c3c9A%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "c5f22dfe-39b3-4a9f-bae4-ab497239320c",
                    "title": "Butterflies",
                    "slug": "salvador-dali-butterflies",
                    "featured": False,
                    "artworksCountMessage": "14 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FEqob_SW84ji3Tc7ClSoonQ%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "19473968-9fe8-4e4d-b2d1-ed222ebbdc2a",
                    "title": "Casanova",
                    "slug": "salvador-dali-casanova",
                    "featured": False,
                    "artworksCountMessage": "10 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FEbCQuJ6DX-M8_wQ9brlsuA%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "98ad6615-de31-466a-a69a-05325ff9864f",
                    "title": "Memories of Surrealism",
                    "slug": "salvador-dali-memories-of-surrealism",
                    "featured": False,
                    "artworksCountMessage": "10 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F4kOy3i3xgtE7-Lqp_FA_5g%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "6d1a5e6a-3413-498c-b21f-07dc0ee35526",
                    "title": "Lobsters",
                    "slug": "salvador-dali-lobsters",
                    "featured": False,
                    "artworksCountMessage": "8 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fp20PCKLZIfN7dkmShWn5kw%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "bffe0fd2-3410-4cc3-87aa-f554f28e1b1d",
                    "title": "Les Diners de Gala",
                    "slug": "salvador-dali-les-diners-de-gala",
                    "featured": False,
                    "artworksCountMessage": "8 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fp20PCKLZIfN7dkmShWn5kw%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "791a89d1-9ba8-4140-a931-9c328a439593",
                    "title": "Poems",
                    "slug": "salvador-dali-poems",
                    "featured": False,
                    "artworksCountMessage": "7 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FALer2U740JGmNqj0UBSrzw%2Flarge.jpg"
                      }
                    }
                  }
                },
                {
                  "node": {
                    "internalID": "519d9289-8296-4161-b9f7-5d4217781532",
                    "title": "Playing Cards",
                    "slug": "salvador-dali-playing-cards",
                    "featured": False,
                    "artworksCountMessage": "2 available",
                    "image": {
                      "cropped": {
                        "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FiX0wSBw4VbvCpmRggO3xUA%2Flarge.jpg"
                      }
                    }
                  }
                }
              ]
            },
            "id": "QXJ0aXN0OjRkYWRjY2U2NzEyOWYwNTkyNDAwMDlkZg=="
          },
          "seriesForCounts": {
            "edges": []
          },
          "pricingContext": None
        },
        "me": None
      }
    }
  ]
]


print(len(dali))
print(len(dali[0]))
print(dali[0][1]["json"]["data"]["artwork"]["images"][0]["url"])
print(dali[0][0])