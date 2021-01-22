#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# change 'true', 'false' and 'null' to 'True', 'False' and 'None'
# deleted from first line of array: "{\"queryID\":\"artworkRoutes_ArtworkQuery\",\"variables\":{\"artworkID\":\"alphonse-mucha-job-30\"}}",
import json

mucha = [
  
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
              "Wed, 20 Jan 2021 19:49:07 GMT"
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
              "W/\"102db-Mm0y15MqVfSL9uXKK8eVZ8RUzHg\""
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
              "slug": "alphonse-mucha-job-30",
              "internalID": "5caba09887748941ee7b1de0",
              "is_acquireable": False,
              "is_offerable": False,
              "availability": "for sale",
              "listPrice": {
                 "__typename": "PriceRange",
                 "display": "$10,000 - 15,000",
                 "minPrice": {
                    "major": 10000,
                    "currencyCode": "USD",
                    "minor": 1000000
                 },
                 "maxPrice": {
                    "major": 15000,
                    "minor": 1500000
                 }
              },
              "is_in_auction": False,
              "sale": None,
              "artists": [
                 {
                    "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                    "slug": "alphonse-mucha",
                    "internalID": "4fbabc998b313700010006da",
                    "name": "Alphonse Mucha",
                    "href": "/artist/alphonse-mucha",
                    "image": {
                       "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=100&height=100&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FPd_DniK14Fp7kZ4sO18fVQ%2Flarge.jpg"
                       }
                    },
                    "formatted_nationality_and_birthday": "Czech, 1860–1939",
                    "counts": {
                       "partner_shows": 24,
                       "follows": 2772
                    },
                    "exhibition_highlights": [
                       {
                          "partner": {
                             "__typename": "Partner",
                             "name": "David Barnett Gallery",
                             "id": "UGFydG5lcjo1YTVmOGNmZjhiM2I4MTQzZTU0OTJmM2I="
                          },
                          "name": "Alphonse Mucha: Art Nouveau",
                          "start_at": "2017",
                          "cover_image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F9n3U-BmG7kIwBtZWHmMxPw%2Flarge.jpg"
                             }
                          },
                          "city": "Milwaukee",
                          "id": "U2hvdzo1YTZjY2YxMjJhODkzYTc4Mzk5Y2M1Y2Y="
                       },
                       {
                          "partner": {
                             "__typename": "Partner",
                             "name": "Rue Royale Fine Art",
                             "id": "UGFydG5lcjo1NDZmN2I5MzcyNjE2OTY2Y2ZlOTAxMDA="
                          },
                          "name": "Celestial Nymphs",
                          "start_at": "2014",
                          "cover_image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fftwed6EP_b9STMNmDeTBsQ%2Flarge.jpg"
                             }
                          },
                          "city": "Las Vegas",
                          "id": "U2hvdzo1NGE3MzMzZTcyNjE2OTQyMmIxNjA4MDA="
                       },
                       {
                          "partner": {
                             "__typename": "Partner",
                             "name": "Larsen Gallery",
                             "id": "UGFydG5lcjo1OGRlZWFiZjJhODkzYTI1OGM2NjFlMTM="
                          },
                          "name": "2020 Fall Larsen Art Auction Post Auction Sale",
                          "start_at": "2020",
                          "cover_image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FN3a4uZhlXrcVGZCzypAgDw%2Flarge.jpg"
                             }
                          },
                          "city": "Scottsdale",
                          "id": "U2hvdzo1Zjk3NjA2NTA3NmJhZTAwMTI0M2QyMzM="
                       }
                    ],
                    "collections": [
                       "Museum of Modern Art (MoMA)"
                    ],
                    "highlights": {
                       "partnersConnection": {
                          "edges": []
                       }
                    },
                    "auctionResultsConnection": None,
                    "biographyBlurb": {
                       "text": "<p>Alphonse Mucha is synonymous with <a href=\"/gene/art-nouveau\">Art Nouveau<\/a>, a style of fine art, decorative art, and architecture that broke with the academicism of the 19th century in favor of florid lines inspired by the natural environment. A lithographed advertising poster he was commissioned to create for a play featuring the celebrated actress Sarah Bernhardt in 1894 catapulted him out of obscurity and brought him instant success as a commercial artist. Rendered in pale pastels, much of his work depicts beautiful young women draped in Neoclassical robes set amidst flowers, feathers, and other sensuous natural forms. He was celebrated not only for illustrating advertising posters, but also for painting, book illustrations, sculpting, and designing theater sets, jewelry, and wallpaper. <\/p>\n"
                    },
                    "is_followed": False,
                    "related": {
                       "suggestedConnection": None
                    },
                    "is_consignable": True
                 }
              ],
              "artist": {
                 "internalID": "4fbabc998b313700010006da",
                 "slug": "alphonse-mucha",
                 "name": "Alphonse Mucha",
                 "href": "/artist/alphonse-mucha",
                 "image": {
                    "cropped": {
                       "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=100&height=100&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FPd_DniK14Fp7kZ4sO18fVQ%2Flarge.jpg"
                    }
                 },
                 "formatted_nationality_and_birthday": "Czech, 1860–1939",
                 "counts": {
                    "partner_shows": 24,
                    "follows": 2772
                 },
                 "exhibition_highlights": [
                    {
                       "partner": {
                          "__typename": "Partner",
                          "name": "David Barnett Gallery",
                          "id": "UGFydG5lcjo1YTVmOGNmZjhiM2I4MTQzZTU0OTJmM2I="
                       },
                       "name": "Alphonse Mucha: Art Nouveau",
                       "start_at": "2017",
                       "cover_image": {
                          "cropped": {
                             "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F9n3U-BmG7kIwBtZWHmMxPw%2Flarge.jpg"
                          }
                       },
                       "city": "Milwaukee",
                       "id": "U2hvdzo1YTZjY2YxMjJhODkzYTc4Mzk5Y2M1Y2Y="
                    },
                    {
                       "partner": {
                          "__typename": "Partner",
                          "name": "Rue Royale Fine Art",
                          "id": "UGFydG5lcjo1NDZmN2I5MzcyNjE2OTY2Y2ZlOTAxMDA="
                       },
                       "name": "Celestial Nymphs",
                       "start_at": "2014",
                       "cover_image": {
                          "cropped": {
                             "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fftwed6EP_b9STMNmDeTBsQ%2Flarge.jpg"
                          }
                       },
                       "city": "Las Vegas",
                       "id": "U2hvdzo1NGE3MzMzZTcyNjE2OTQyMmIxNjA4MDA="
                    },
                    {
                       "partner": {
                          "__typename": "Partner",
                          "name": "Larsen Gallery",
                          "id": "UGFydG5lcjo1OGRlZWFiZjJhODkzYTI1OGM2NjFlMTM="
                       },
                       "name": "2020 Fall Larsen Art Auction Post Auction Sale",
                       "start_at": "2020",
                       "cover_image": {
                          "cropped": {
                             "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FN3a4uZhlXrcVGZCzypAgDw%2Flarge.jpg"
                          }
                       },
                       "city": "Scottsdale",
                       "id": "U2hvdzo1Zjk3NjA2NTA3NmJhZTAwMTI0M2QyMzM="
                    }
                 ],
                 "collections": [
                    "Museum of Modern Art (MoMA)"
                 ],
                 "highlights": {
                    "partnersConnection": {
                       "edges": []
                    }
                 },
                 "auctionResultsConnection": None,
                 "biographyBlurb": {
                    "text": "<p>Alphonse Mucha is synonymous with <a href=\"/gene/art-nouveau\">Art Nouveau<\/a>, a style of fine art, decorative art, and architecture that broke with the academicism of the 19th century in favor of florid lines inspired by the natural environment. A lithographed advertising poster he was commissioned to create for a play featuring the celebrated actress Sarah Bernhardt in 1894 catapulted him out of obscurity and brought him instant success as a commercial artist. Rendered in pale pastels, much of his work depicts beautiful young women draped in Neoclassical robes set amidst flowers, feathers, and other sensuous natural forms. He was celebrated not only for illustrating advertising posters, but also for painting, book illustrations, sculpting, and designing theater sets, jewelry, and wallpaper. <\/p>\n"
                 },
                 "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
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
                                "name": "A.M. Cassandre",
                                "slug": "am-cassandre",
                                "href": "/artist/am-cassandre",
                                "image": {
                                   "cropped": {
                                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FtahOUuHJ9BgRev8eBzlkTw%2Flarge.jpg"
                                   }
                                },
                                "formatted_nationality_and_birthday": "French, 1901–1968",
                                "id": "QXJ0aXN0OjU5Mjc4OGYwMmE4OTNhMmE3NjFlMmM4Ng==",
                                "internalID": "592788f02a893a2a761e2c86",
                                "is_followed": False,
                                "counts": {
                                   "follows": 201
                                },
                                "__typename": "Artist"
                             },
                             "cursor": "YXJyYXljb25uZWN0aW9uOjA="
                          },
                          {
                             "node": {
                                "name": "Henri-Gustave Jossot",
                                "slug": "henri-gustave-jossot",
                                "href": "/artist/henri-gustave-jossot",
                                "image": {
                                   "cropped": {
                                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FCyC6W7g7v1MYwMn4xuWpFw%2Flarge.jpg"
                                   }
                                },
                                "formatted_nationality_and_birthday": "",
                                "id": "QXJ0aXN0OjU3NjAxMDJlNzYyMmRkNjVkZjAwMDI5Yw==",
                                "internalID": "5760102e7622dd65df00029c",
                                "is_followed": False,
                                "counts": {
                                   "follows": 80
                                },
                                "__typename": "Artist"
                             },
                             "cursor": "YXJyYXljb25uZWN0aW9uOjE="
                          },
                          {
                             "node": {
                                "name": "Georges de Feure",
                                "slug": "georges-de-feure",
                                "href": "/artist/georges-de-feure",
                                "image": {
                                   "cropped": {
                                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FraDWU4JfDqepE0urJ6QUHQ%2Flarge.jpg"
                                   }
                                },
                                "formatted_nationality_and_birthday": "French, 1868–1928",
                                "id": "QXJ0aXN0OjUyYTEwODAyMTM5YjIxYTY3ZTAwMDE5Mw==",
                                "internalID": "52a10802139b21a67e000193",
                                "is_followed": False,
                                "counts": {
                                   "follows": 161
                                },
                                "__typename": "Artist"
                             },
                             "cursor": "YXJyYXljb25uZWN0aW9uOjI="
                          },
                          {
                             "node": {
                                "name": "Louis Abel-Truchet",
                                "slug": "louis-abel-truchet",
                                "href": "/artist/louis-abel-truchet",
                                "image": {
                                   "cropped": {
                                      "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FwPAWlY-yXlp4_kNaGLT8_w%2Flarge.jpg"
                                   }
                                },
                                "formatted_nationality_and_birthday": "French, 1857–1918",
                                "id": "QXJ0aXN0OjUyYTEwNzZiOGIzYjgxYzc0MjAwMDE5ZQ==",
                                "internalID": "52a1076b8b3b81c74200019e",
                                "is_followed": False,
                                "counts": {
                                   "follows": 118
                                },
                                "__typename": "Artist"
                             },
                             "cursor": "YXJyYXljb25uZWN0aW9uOjM="
                          }
                       ]
                    }
                 }
              },
              "href": "/artwork/alphonse-mucha-job-30",
              "date": "1900",
              "artist_names": "Alphonse Mucha",
              "sale_message": "$10,000 - 15,000",
              "partner": {
                 "name": "Galerie d'Orsay",
                 "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
                 "type": "Gallery",
                 "profile": {
                    "image": {
                       "resized": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FxtN5t2O49vsCc07XP4wopQ%2Fwide.jpg"
                       }
                    },
                    "id": "UHJvZmlsZTo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmY=",
                    "slug": "galerie-dorsay",
                    "name": "Galerie d'Orsay",
                    "internalID": "557f1a92776f7260b20000ff",
                    "is_followed": False,
                    "icon": {
                       "url": "https://d32dm0rphc51dk.cloudfront.net/SjLYl9ZCWlfGZx2NCc4NKQ/square140.png"
                    }
                 },
                 "initials": "GO",
                 "href": "/galerie-dorsay",
                 "locations": [
                    {
                       "city": "Boston",
                       "id": "TG9jYXRpb246NTg3NjljMmVhMDlhNjczN2ZlMDAxMDEy"
                    }
                 ],
                 "isVerifiedSeller": False,
                 "internalID": "557f1a92776f7260b20000fd",
                 "slug": "galerie-dorsay",
                 "is_default_profile_public": True
              },
              "image_rights": "",
              "is_shareable": True,
              "meta_image": {
                 "resized": {
                    "width": 640,
                    "height": 824,
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=640&height=824&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fz6cZrfbgQXCnoZPztYQTsQ%2Flarge.jpg"
                 }
              },
              "meta": {
                 "title": "Alphonse Mucha | Job (1900) | Available for Sale | Artsy",
                 "description": "Available for sale from Galerie d'Orsay, Alphonse Mucha, Job (1900), Lithograph on wove paper, 11 1/2 × 8 7/8 in",
                 "long_description": "Available for sale from Galerie d'Orsay, Alphonse Mucha, Job (1900), Lithograph on wove paper, 11 1/2 × 8 7/8 in"
              },
              "context": {
                 "__typename": "Show",
                 "id": "U2hvdzo1ZWMwNjBjNGFkNmQyOTAwMGVkNDY2MTQ=",
                 "name": "Galerie d'Orsay: Celebrating Twenty Years & Counting!",
                 "href": "/show/galerie-dorsay-galerie-dorsay-celebrating-twenty-years-and-counting",
                 "status": "closed",
                 "thumbnail": {
                    "img": {
                       "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=70&height=70&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fd-Opl4tVJi1OHlBYzkhcNw%2Fsquare.jpg"
                    }
                 }
              },
              "is_price_hidden": False,
              "is_price_range": True,
              "category": "Print",
              "dimensions": {
                 "in": "11 1/2 × 8 7/8 in",
                 "cm": "29.2 × 22.5 cm"
              },
              "cultural_maker": None,
              "is_biddable": False,
              "edition_sets": [],
              "sale_artwork": None,
              "title": "Job",
              "medium": "Lithograph on wove paper",
              "edition_of": None,
              "attributionClass": {
                 "shortDescription": "This work is from an edition of unknown size",
                 "id": "QXR0cmlidXRpb25DbGFzczp1bmtub3duIGVkaXRpb24="
              },
              "myLotStanding": None,
              "is_for_sale": True,
              "is_inquireable": True,
              "priceIncludesTaxDisplay": None,
              "shippingInfo": "Shipping, tax, and additional fees quoted by seller",
              "shippingOrigin": "Boston, MA, US",
              "hasCertificateOfAuthenticity": True,
              "description": None,
              "additional_information": None,
              "series": "Masters of the Poster",
              "publisher": "Published by Jules Chéret; printed at Impremiere Chaix (Atelier Chéret), Paris.",
              "manufacturer": None,
              "canRequestLotConditionsReport": False,
              "framed": {
                 "label": "Framed",
                 "details": "Included"
              },
              "signatureInfo": {
                 "label": "Signature",
                 "details": "Signed on the stone lower right Mucha"
              },
              "conditionDescription": {
                 "label": "Condition details",
                 "details": "In excellent condition, with bright, fresh colors, printed on a sheet with full margins."
              },
              "certificateOfAuthenticity": {
                 "label": "Certificate of authenticity",
                 "details": "Included"
              },
              "mediumType": {
                 "__typename": "ArtworkMedium",
                 "name": "Print",
                 "longDescription": "Includes etchings; engravings; lithographs; monoprints; screen prints; woodcuts."
              },
              "articles": [],
              "literature": None,
              "exhibition_history": None,
              "provenance": None,
              "image_alt": "Alphonse Mucha, ‘Job’, 1900, Galerie d'Orsay",
              "id": "QXJ0d29yazo1Y2FiYTA5ODg3NzQ4OTQxZWU3YjFkZTA=",
              "is_saved": False,
              "images": [
                 {
                    "url": "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/larger.jpg",
                    "internalID": "5caba09987748941ee7b1de6",
                    "uri": "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/large.jpg",
                    "placeholder": {
                       "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=30&height=38&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fz6cZrfbgQXCnoZPztYQTsQ%2Fsmall.jpg"
                    },
                    "aspectRatio": 0.78,
                    "is_zoomable": True,
                    "is_default": True,
                    "deepZoom": {
                       "Image": {
                          "xmlns": "http://schemas.microsoft.com/deepzoom/2008",
                          "Url": "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/dztiles/",
                          "Format": "jpg",
                          "TileSize": 512,
                          "Overlap": 0,
                          "Size": {
                             "Width": 1128,
                             "Height": 1454
                          }
                       }
                    }
                 }
              ],
              "artworkMeta": {
                 "share": "Check out Alphonse Mucha, Job (1900), From Galerie d'Orsay"
              },
              "image": {
                 "internalID": "5caba09987748941ee7b1de6",
                 "url": "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/larger.jpg",
                 "height": 1454,
                 "width": 1128
              },
              "is_downloadable": False,
              "is_hangable": True,
              "contextGrids": [
                 {
                    "__typename": "ShowArtworkGrid",
                    "title": "Other works from Galerie d'Orsay: Celebrating Twenty Years & Counting!",
                    "ctaTitle": "View all works from the show",
                    "ctaHref": "/show/galerie-dorsay-galerie-dorsay-celebrating-twenty-years-and-counting",
                    "artworksConnection": {
                       "edges": [
                          {
                             "__typename": "ArtworkEdge",
                             "node": {
                                "id": "QXJ0d29yazo1ZWM1YTdlZDBhZDIyMDAwMGRiNWVmMmU=",
                                "slug": "pierre-auguste-renoir-lenfant-au-biscuit-jean-renoir-5",
                                "href": "/artwork/pierre-auguste-renoir-lenfant-au-biscuit-jean-renoir-5",
                                "internalID": "5ec5a7ed0ad220000db5ef2e",
                                "image": {
                                   "aspect_ratio": 0.82,
                                   "placeholder": "121.73913043478262%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/vSfSCiWOK7k3PLzOL5BVJQ/large.jpg"
                                },
                                "title": "L'Enfant au Biscuit (Jean Renoir)",
                                "image_title": "Pierre-Auguste Renoir, ‘L'Enfant au Biscuit (Jean Renoir)’, 1841-1919",
                                "date": "1841-1919",
                                "sale_message": "$30,000 - 40,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRkOGI5MjljNGViNjhhMWIyYzAwMDJlMA==",
                                      "href": "/artist/pierre-auguste-renoir",
                                      "name": "Pierre-Auguste Renoir"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ODgzOWJkYzc2MjJkZDExOTgwMDAxNzA=",
                                "slug": "edouard-manet-jeanne-le-printemps",
                                "href": "/artwork/edouard-manet-jeanne-le-printemps",
                                "internalID": "58839bdc7622dd1198000170",
                                "image": {
                                   "aspect_ratio": 0.8,
                                   "placeholder": "125.7510729613734%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/ebElhRb46RXI3WgRzPryVQ/large.jpg"
                                },
                                "title": "Jeanne (Le Printemps)",
                                "image_title": "Édouard Manet, ‘Jeanne (Le Printemps)’, 1882",
                                "date": "1882",
                                "sale_message": "$7,500 - 10,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRkOGI5MjdlNGViNjhhMWIyYzAwMDE2OA==",
                                      "href": "/artist/edouard-manet",
                                      "name": "Édouard Manet"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZWM1YTI5ZDRhOGMzNDAwMGVmMDMxOTY=",
                                "slug": "georges-rouault-parade",
                                "href": "/artwork/georges-rouault-parade",
                                "internalID": "5ec5a29d4a8c34000ef03196",
                                "image": {
                                   "aspect_ratio": 0.65,
                                   "placeholder": "152.8013582342954%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/00XmFFxH7qCkrTE1W0Ckzg/large.jpg"
                                },
                                "title": "Parade",
                                "image_title": "Georges Rouault, ‘Parade’, 1934",
                                "date": "1934",
                                "sale_message": "$150,000 - 200,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRlOTc2NDllNmJhNzEyMDAwMTAwMjM1OA==",
                                      "href": "/artist/georges-rouault",
                                      "name": "Georges Rouault"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZWM1YTI5OTVkNGE5ODAwMTIxMDEyNjk=",
                                "slug": "georges-rouault-clown-et-enfant-2",
                                "href": "/artwork/georges-rouault-clown-et-enfant-2",
                                "internalID": "5ec5a2995d4a980012101269",
                                "image": {
                                   "aspect_ratio": 0.69,
                                   "placeholder": "144.23076923076923%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/1IW0xmaa2AUlNe8jyxOFww/large.jpg"
                                },
                                "title": "Clown et Enfant",
                                "image_title": "Georges Rouault, ‘Clown et Enfant’, 1930",
                                "date": "1930",
                                "sale_message": "$7,500 - 10,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRlOTc2NDllNmJhNzEyMDAwMTAwMjM1OA==",
                                      "href": "/artist/georges-rouault",
                                      "name": "Georges Rouault"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZTFjYmQxMjE0N2U4MzAwMTIwOTViNmE=",
                                "slug": "henri-de-toulouse-lautrec-divan-japonais-27",
                                "href": "/artwork/henri-de-toulouse-lautrec-divan-japonais-27",
                                "internalID": "5e1cbd12147e830012095b6a",
                                "image": {
                                   "aspect_ratio": 0.75,
                                   "placeholder": "132.95687885010267%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/rOgztp20GC_ul-Am9RgUgg/large.jpg"
                                },
                                "title": "Divan Japonais",
                                "image_title": "Henri de Toulouse-Lautrec, ‘Divan Japonais’, 1895",
                                "date": "1895",
                                "sale_message": "$7,500 - 10,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRlZGY5Yjg4OTAxOTJiMDAwMTAwMTc4OQ==",
                                      "href": "/artist/henri-de-toulouse-lautrec",
                                      "name": "Henri de Toulouse-Lautrec"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ODgzZDRiYzEzOWIyMTAzMWUwMDM1Y2U=",
                                "slug": "henri-de-toulouse-lautrec-jane-avril-jardin-de-paris",
                                "href": "/artwork/henri-de-toulouse-lautrec-jane-avril-jardin-de-paris",
                                "internalID": "5883d4bc139b21031e0035ce",
                                "image": {
                                   "aspect_ratio": 0.75,
                                   "placeholder": "133.48017621145374%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/yVf2v4G-QgEbnDDbdTMF3w/large.jpg"
                                },
                                "title": "Jane Avril - Jardin De Paris",
                                "image_title": "Henri de Toulouse-Lautrec, ‘Jane Avril - Jardin De Paris’, 1898",
                                "date": "1898",
                                "sale_message": "$7,500 - 10,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRlZGY5Yjg4OTAxOTJiMDAwMTAwMTc4OQ==",
                                      "href": "/artist/henri-de-toulouse-lautrec",
                                      "name": "Henri de Toulouse-Lautrec"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZTFmZGE1NDQzMTBjODAwMGZkZDI4OTY=",
                                "slug": "mary-cassatt-the-crocheting-lesson-4",
                                "href": "/artwork/mary-cassatt-the-crocheting-lesson-4",
                                "internalID": "5e1fda544310c8000fdd2896",
                                "image": {
                                   "aspect_ratio": 0.61,
                                   "placeholder": "164.23357664233578%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/PXp_1k6FhInyZzv99M6XzQ/large.jpg"
                                },
                                "title": "The Crocheting Lesson",
                                "image_title": "Mary Cassatt, ‘The Crocheting Lesson’, 1902",
                                "date": "1902",
                                "sale_message": "$40,000 - 50,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRkOGI5MmI3NGViNjhhMWIyYzAwMDQxZQ==",
                                      "href": "/artist/mary-cassatt",
                                      "name": "Mary Cassatt"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1Y2FiYTAzNTMyYzI5NTMyM2JkNjU2MzM=",
                                "slug": "alphonse-mucha-salon-des-cents",
                                "href": "/artwork/alphonse-mucha-salon-des-cents",
                                "internalID": "5caba03532c295323bd65633",
                                "image": {
                                   "aspect_ratio": 0.67,
                                   "placeholder": "148.5148514851485%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/zVERnQ3TkrYJcokNH6K3yA/large.jpg"
                                },
                                "title": "Salon Des Cents",
                                "image_title": "Alphonse Mucha, ‘Salon Des Cents’, 1897",
                                "date": "1897",
                                "sale_message": "$7,500 - 10,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                    "__typename": "ArtistArtworkGrid",
                    "title": "Other works by Alphonse Mucha",
                    "ctaTitle": "View all works by Alphonse Mucha",
                    "ctaHref": "/artist/alphonse-mucha",
                    "artworksConnection": {
                       "edges": [
                          {
                             "__typename": "ArtworkEdge",
                             "node": {
                                "id": "QXJ0d29yazo1M2NlYmU1MDcyNjE2OTQyNDcxMDAxMDA=",
                                "slug": "alphonse-mucha-lorenzaccio",
                                "href": "/artwork/alphonse-mucha-lorenzaccio",
                                "internalID": "53cebe507261694247100100",
                                "image": {
                                   "aspect_ratio": 0.38,
                                   "placeholder": "263.15789473684214%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/H-x6cmA8HIiTQO9JTR51NA/large.jpg"
                                },
                                "title": "LORENZACCIO",
                                "image_title": "Alphonse Mucha, ‘LORENZACCIO’, 1898",
                                "date": "1898",
                                "sale_message": "Contact For Price",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Christopher-Clark Fine Art",
                                   "href": "/christopher-clark-fine-art",
                                   "id": "UGFydG5lcjo1MmIyMGY1NDEzOWIyMTQyYzQwMDAwNGQ=",
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
                                "id": "QXJ0d29yazo1MjVkN2FlZTc2MjJkZGU1NGUwMDAxYjY=",
                                "slug": "alphonse-mucha-la-samaritaine",
                                "href": "/artwork/alphonse-mucha-la-samaritaine",
                                "internalID": "525d7aee7622dde54e0001b6",
                                "image": {
                                   "aspect_ratio": 0.65,
                                   "placeholder": "152.83842794759826%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/Me8KG4eU7acHbNdxVQRYJA/large.jpg"
                                },
                                "title": "La Samaritaine",
                                "image_title": "Alphonse Mucha, ‘La Samaritaine’, 1899",
                                "date": "1899",
                                "sale_message": "Contact For Price",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Contessa Gallery",
                                   "href": "/contessa-gallery",
                                   "id": "UGFydG5lcjo1MjRiNDRhNjljMThkYjllZmEwMDAwZjI=",
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
                                "id": "QXJ0d29yazo1ZDk2MzBiYjVmZjMzOTAwMTM3NjU2MGI=",
                                "slug": "alphonse-mucha-job-21",
                                "href": "/artwork/alphonse-mucha-job-21",
                                "internalID": "5d9630bb5ff339001376560b",
                                "image": {
                                   "aspect_ratio": 0.65,
                                   "placeholder": "153.57142857142858%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/eLndsQDFY_lb6FkaAkt7nA/large.jpg"
                                },
                                "title": "Job",
                                "image_title": "Alphonse Mucha, ‘Job’, 1898",
                                "date": "1898",
                                "sale_message": None,
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Isselbacher Gallery",
                                   "href": "/isselbacher-gallery",
                                   "id": "UGFydG5lcjo1OTc5MDFmY2FiNjBjYTYwZDI0NmNmZTE=",
                                   "type": "Gallery"
                                },
                                "sale": None,
                                "sale_artwork": None,
                                "is_inquireable": False,
                                "is_saved": False,
                                "is_biddable": False
                             }
                          },
                          {
                             "__typename": "ArtworkEdge",
                             "node": {
                                "id": "QXJ0d29yazo1YmEwMGZjMTYwY2FkOTVhMGJkYTIyM2Q=",
                                "slug": "alphonse-mucha-lorenzaccio-3",
                                "href": "/artwork/alphonse-mucha-lorenzaccio-3",
                                "internalID": "5ba00fc160cad95a0bda223d",
                                "image": {
                                   "aspect_ratio": 0.57,
                                   "placeholder": "175.31468531468533%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/yOEzUSGFBbGBtqhTLa157w/large.jpg"
                                },
                                "title": "Lorenzaccio",
                                "image_title": "Alphonse Mucha, ‘Lorenzaccio’",
                                "date": "",
                                "sale_message": None,
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Hindman",
                                   "href": "/auction/leslie-hindman-auctioneers",
                                   "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                   "type": "Auction House"
                                },
                                "sale": {
                                   "is_auction": True,
                                   "is_closed": True,
                                   "id": "U2FsZTo1YjlhYjhmNTI4MzViNDYzM2IyZmQ0ZDg=",
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
                                      "display": "$250"
                                   },
                                   "id": "U2FsZUFydHdvcms6NWJhMDBmYzI3YWY4NmIwNjQyOTYzZTU2"
                                },
                                "is_inquireable": False,
                                "is_saved": False,
                                "is_biddable": False
                             }
                          },
                          {
                             "__typename": "ArtworkEdge",
                             "node": {
                                "id": "QXJ0d29yazo1YmEwMGZlNWRhMDFiNDFjYmUzNzA5YmY=",
                                "slug": "alphonse-mucha-chansons-daieules",
                                "href": "/artwork/alphonse-mucha-chansons-daieules",
                                "internalID": "5ba00fe5da01b41cbe3709bf",
                                "image": {
                                   "aspect_ratio": 0.73,
                                   "placeholder": "136.92762186115215%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/LhLdQXWyB-08UJdfO4BHXw/large.jpg"
                                },
                                "title": "Chansons d'Aieules",
                                "image_title": "Alphonse Mucha, ‘Chansons d'Aieules’",
                                "date": "",
                                "sale_message": None,
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Hindman",
                                   "href": "/auction/leslie-hindman-auctioneers",
                                   "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                   "type": "Auction House"
                                },
                                "sale": {
                                   "is_auction": True,
                                   "is_closed": True,
                                   "id": "U2FsZTo1YjlhYjhmNTI4MzViNDYzM2IyZmQ0ZDg=",
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
                                      "display": "$400"
                                   },
                                   "id": "U2FsZUFydHdvcms6NWJhMDBmZTYxNjc5NWMyZWY0MDA3ZjA4"
                                },
                                "is_inquireable": False,
                                "is_saved": False,
                                "is_biddable": False
                             }
                          },
                          {
                             "__typename": "ArtworkEdge",
                             "node": {
                                "id": "QXJ0d29yazo1YmExMmUwYjA5NjQxNzFjNjhhMTFiMTM=",
                                "slug": "alphonse-mucha-lautomne",
                                "href": "/artwork/alphonse-mucha-lautomne",
                                "internalID": "5ba12e0b0964171c68a11b13",
                                "image": {
                                   "aspect_ratio": 0.43,
                                   "placeholder": "231.8579766536965%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/d5a2sVRnEaxj8u1nfcLMYg/large.jpg"
                                },
                                "title": "L'Automne",
                                "image_title": "Alphonse Mucha, ‘L'Automne’, c. 1903",
                                "date": "c. 1903",
                                "sale_message": None,
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Hindman",
                                   "href": "/auction/leslie-hindman-auctioneers",
                                   "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                   "type": "Auction House"
                                },
                                "sale": {
                                   "is_auction": True,
                                   "is_closed": True,
                                   "id": "U2FsZTo1YmEwMTg5OTJiMmZlZjAwMjkxZWNiMDk=",
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
                                      "display": "$120"
                                   },
                                   "opening_bid": {
                                      "display": "$100"
                                   },
                                   "id": "U2FsZUFydHdvcms6NWJhMTJlMGVhZGJlYzczZTQ3ZDIxYzBk"
                                },
                                "is_inquireable": False,
                                "is_saved": False,
                                "is_biddable": False
                             }
                          },
                          {
                             "__typename": "ArtworkEdge",
                             "node": {
                                "id": "QXJ0d29yazo1M2NlYmU1ZjcyNjE2OTQyNDcxYTAxMDA=",
                                "slug": "alphonse-mucha-la-dame-aux-camelias",
                                "href": "/artwork/alphonse-mucha-la-dame-aux-camelias",
                                "internalID": "53cebe5f72616942471a0100",
                                "image": {
                                   "aspect_ratio": 0.38,
                                   "placeholder": "263.15789473684214%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/DmXSXMSGpo5fGT0WKc3uYg/large.jpg"
                                },
                                "title": "La Dame Aux Camélias",
                                "image_title": "Alphonse Mucha, ‘La Dame Aux Camélias’, 1898",
                                "date": "1898",
                                "sale_message": "Contact For Price",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Christopher-Clark Fine Art",
                                   "href": "/christopher-clark-fine-art",
                                   "id": "UGFydG5lcjo1MmIyMGY1NDEzOWIyMTQyYzQwMDAwNGQ=",
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
                                "id": "QXJ0d29yazo1Y2QxZTBmNzc4N2Q0ZTAwMTI1NGZkOTI=",
                                "slug": "alphonse-mucha-the-seasons-a-suite-of-four-works",
                                "href": "/artwork/alphonse-mucha-the-seasons-a-suite-of-four-works",
                                "internalID": "5cd1e0f7787d4e001254fd92",
                                "image": {
                                   "aspect_ratio": 0.52,
                                   "placeholder": "193.71794871794873%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/MzMOn0ZxhKjaVkq54qQ8Hg/large.jpg"
                                },
                                "title": "The Seasons  (a suite of four works)",
                                "image_title": "Alphonse Mucha, ‘The Seasons  (a suite of four works)’, 1896",
                                "date": "1896",
                                "sale_message": None,
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                      "href": "/artist/alphonse-mucha",
                                      "name": "Alphonse Mucha"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Hindman",
                                   "href": "/auction/leslie-hindman-auctioneers",
                                   "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                   "type": "Auction House"
                                },
                                "sale": {
                                   "is_auction": True,
                                   "is_closed": True,
                                   "id": "U2FsZTo1Y2QwNGY0ZDg3MzU4NTFkMDliM2QxNTg=",
                                   "is_live_open": False,
                                   "is_open": False,
                                   "is_preview": False,
                                   "display_timely_at": None
                                },
                                "sale_artwork": {
                                   "counts": {
                                      "bidder_positions": 1
                                   },
                                   "highest_bid": {
                                      "display": "$6,000"
                                   },
                                   "opening_bid": {
                                      "display": "$6,000"
                                   },
                                   "id": "U2FsZUFydHdvcms6NWNkMWUwZjgyODdmMWE0ZjdjNWNlMzA2"
                                },
                                "is_inquireable": False,
                                "is_saved": False,
                                "is_biddable": False
                             }
                          }
                       ]
                    }
                 },
                 {
                    "__typename": "PartnerArtworkGrid",
                    "title": "Other works from Galerie d'Orsay",
                    "ctaTitle": "View all works from Galerie d'Orsay",
                    "ctaHref": "/galerie-dorsay",
                    "artworksConnection": {
                       "edges": [
                          {
                             "__typename": "ArtworkEdge",
                             "node": {
                                "id": "QXJ0d29yazo1ZmQzYWY1M2RlNTg1OTAwMTI3ZTMyY2Y=",
                                "slug": "ken-salaz-sunrise-over-walden-pond",
                                "href": "/artwork/ken-salaz-sunrise-over-walden-pond",
                                "internalID": "5fd3af53de585900127e32cf",
                                "image": {
                                   "aspect_ratio": 1.63,
                                   "placeholder": "61.4%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/suUXEypO9xJsYPj51uPMHQ/large.jpg"
                                },
                                "title": "Sunrise over Walden Pond",
                                "image_title": "Ken Salaz, ‘Sunrise over Walden Pond’, 2020",
                                "date": "2020",
                                "sale_message": "$2,500 - 5,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjU1NTRkYTQ5NzI2MTY5MGRhYTdkMDAwMA==",
                                      "href": "/artist/ken-salaz",
                                      "name": "Ken Salaz"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZmQzYWY1MjUzMGRmMDAwMTFjZDY5NGI=",
                                "slug": "ken-salaz-sunflare-off-walden-pond",
                                "href": "/artwork/ken-salaz-sunflare-off-walden-pond",
                                "internalID": "5fd3af52530df00011cd694b",
                                "image": {
                                   "aspect_ratio": 1.36,
                                   "placeholder": "73.32878581173262%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/hb8G9_s9wD1tgtXojA3Whw/large.jpg"
                                },
                                "title": "Sunflare off Walden Pond",
                                "image_title": "Ken Salaz, ‘Sunflare off Walden Pond’, 2020",
                                "date": "2020",
                                "sale_message": "$2,500 - 5,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjU1NTRkYTQ5NzI2MTY5MGRhYTdkMDAwMA==",
                                      "href": "/artist/ken-salaz",
                                      "name": "Ken Salaz"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZmQzYWY1MzAxY2I4YzAwMTI1NjM2YjQ=",
                                "slug": "ken-salaz-afternoon-sunlight-stroll-walden",
                                "href": "/artwork/ken-salaz-afternoon-sunlight-stroll-walden",
                                "internalID": "5fd3af5301cb8c00125636b4",
                                "image": {
                                   "aspect_ratio": 1.32,
                                   "placeholder": "75.66433566433567%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/NGC_LAwvOKejDKL43bTeKQ/large.jpg"
                                },
                                "title": "Afternoon Sunlight Stroll - Walden",
                                "image_title": "Ken Salaz, ‘Afternoon Sunlight Stroll - Walden’, 2020",
                                "date": "2020",
                                "sale_message": "$2,500 - 5,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjU1NTRkYTQ5NzI2MTY5MGRhYTdkMDAwMA==",
                                      "href": "/artist/ken-salaz",
                                      "name": "Ken Salaz"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZmQzYWY1MjEyZDE1OTQxMDA4OTc2NWU=",
                                "slug": "ken-salaz-journey-home",
                                "href": "/artwork/ken-salaz-journey-home",
                                "internalID": "5fd3af5212d159410089765e",
                                "image": {
                                   "aspect_ratio": 2.02,
                                   "placeholder": "49.6%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/kZJhOerwVdMKXVldaT4mGg/large.jpg"
                                },
                                "title": "Journey Home",
                                "image_title": "Ken Salaz, ‘Journey Home’, 2013",
                                "date": "2013",
                                "sale_message": "$7,500 - 10,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjU1NTRkYTQ5NzI2MTY5MGRhYTdkMDAwMA==",
                                      "href": "/artist/ken-salaz",
                                      "name": "Ken Salaz"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZmQzYWY3MzkxYWRiZjAwMTJlMGJiY2U=",
                                "slug": "damien-hirst-histidyl-7",
                                "href": "/artwork/damien-hirst-histidyl-7",
                                "internalID": "5fd3af7391adbf0012e0bbce",
                                "image": {
                                   "aspect_ratio": 1.26,
                                   "placeholder": "79.22222222222223%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/6mIxd08Z9PFZ2LHNKsytFQ/large.jpg"
                                },
                                "title": "Histidyl",
                                "image_title": "Damien Hirst, ‘Histidyl’, 2008",
                                "date": "2008",
                                "sale_message": "$15,000 - 20,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRkOGI5MjZhNGViNjhhMWIyYzAwMDBhZQ==",
                                      "href": "/artist/damien-hirst",
                                      "name": "Damien Hirst"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZmJhYTk4YjU0MDg1ZTAwMGU3YmNkOWQ=",
                                "slug": "salvador-dali-turtle-mountain-1",
                                "href": "/artwork/salvador-dali-turtle-mountain-1",
                                "internalID": "5fbaa98b54085e000e7bcd9d",
                                "image": {
                                   "aspect_ratio": 0.76,
                                   "placeholder": "131.67587476979742%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/N6skYA7GBaTf_q87ui104w/large.jpg"
                                },
                                "title": "Turtle Mountain",
                                "image_title": "Salvador Dalí, ‘Turtle Mountain’, 1967",
                                "date": "1967",
                                "sale_message": "$2,500 - 5,000",
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
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZmJhYTk4YjQyNjBlZDNjY2NkOWYzOTI=",
                                "slug": "salvador-dali-magic-circle",
                                "href": "/artwork/salvador-dali-magic-circle",
                                "internalID": "5fbaa98b4260ed3cccd9f392",
                                "image": {
                                   "aspect_ratio": 0.58,
                                   "placeholder": "171.875%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/vuop_F876C8GrpDcpWH5QQ/large.jpg"
                                },
                                "title": "Magic Circle",
                                "image_title": "Salvador Dalí, ‘Magic Circle’, 1968",
                                "date": "1968",
                                "sale_message": "$5,000 - 7,500",
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
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1ZmJhYTk4YjRkZWNhZDAwMTJiYzZiN2Y=",
                                "slug": "salvador-dali-petite-horses-1",
                                "href": "/artwork/salvador-dali-petite-horses-1",
                                "internalID": "5fbaa98b4decad0012bc6b7f",
                                "image": {
                                   "aspect_ratio": 0.73,
                                   "placeholder": "136.6742596810934%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/Z1iNXjNULNlfF9KDRL0ktg/large.jpg"
                                },
                                "title": "Petite Horses",
                                "image_title": "Salvador Dalí, ‘Petite Horses’, 1967",
                                "date": "1967",
                                "sale_message": "$7,500 - 10,000",
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
                                   "name": "Galerie d'Orsay",
                                   "href": "/galerie-dorsay",
                                   "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                                "id": "QXJ0d29yazo1MjVkN2RiMjljMThkYjY2YzUwMDA2YWU=",
                                "slug": "pierre-auguste-renoir-claude-renoir-tourne-a-gauche",
                                "href": "/artwork/pierre-auguste-renoir-claude-renoir-tourne-a-gauche",
                                "internalID": "525d7db29c18db66c50006ae",
                                "image": {
                                   "aspect_ratio": 0.84,
                                   "placeholder": "119.65811965811966%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/_TNO-d0fxLDqPZbSNU6VIg/large.jpg"
                                },
                                "title": "Claude Renoir, Tourne a Gauche",
                                "image_title": "Pierre-Auguste Renoir, ‘Claude Renoir, Tourne a Gauche’, ca. 1904",
                                "date": "ca. 1904",
                                "sale_message": "Contact For Price",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRkOGI5MjljNGViNjhhMWIyYzAwMDJlMA==",
                                      "href": "/artist/pierre-auguste-renoir",
                                      "name": "Pierre-Auguste Renoir"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Contessa Gallery",
                                   "href": "/contessa-gallery",
                                   "id": "UGFydG5lcjo1MjRiNDRhNjljMThkYjllZmEwMDAwZjI=",
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
                                "id": "QXJ0d29yazo1OGY3ZWYzNzI3NWIyNDAzY2Q1MDU0Zjc=",
                                "slug": "henri-matisse-visage-legerement-penche-vers-la-gauche-8",
                                "href": "/artwork/henri-matisse-visage-legerement-penche-vers-la-gauche-8",
                                "internalID": "58f7ef37275b2403cd5054f7",
                                "image": {
                                   "aspect_ratio": 0.66,
                                   "placeholder": "152.0190023752969%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/RRa4bmBuDuW-srVcciKAkg/large.jpg"
                                },
                                "title": "Visage Légèrement Penché vers la Gauche",
                                "image_title": "Henri Matisse, ‘Visage Légèrement Penché vers la Gauche’, 1913",
                                "date": "1913",
                                "sale_message": "Contact For Price",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRkOGI5MjkzNGViNjhhMWIyYzAwMDI1YQ==",
                                      "href": "/artist/henri-matisse",
                                      "name": "Henri Matisse"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie Maximillian",
                                   "href": "/galerie-maximillian",
                                   "id": "UGFydG5lcjo1MmZhNDZjNWM5ZGMyNDcxNzcwMDAxNzM=",
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
                                "id": "QXJ0d29yazo1YTc4YjE4MTJhODkzYTYwNzllN2M4YjU=",
                                "slug": "alfred-kubin-der-beste-arzt",
                                "href": "/artwork/alfred-kubin-der-beste-arzt",
                                "internalID": "5a78b1812a893a6079e7c8b5",
                                "image": {
                                   "aspect_ratio": 1.33,
                                   "placeholder": "75%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/uXKNQamSIurz5QuKOVR2HQ/large.jpg"
                                },
                                "title": "Der Beste Arzt",
                                "image_title": "Alfred Kubin, ‘Der Beste Arzt’, 1900-1909",
                                "date": "1900-1909",
                                "sale_message": "Sold",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjUwNmIzYTBjN2VkYzg5MDAwMjAwMGRhZA==",
                                      "href": "/artist/alfred-kubin",
                                      "name": "Alfred Kubin"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Lions Gallery",
                                   "href": "/lions-gallery",
                                   "id": "UGFydG5lcjo1YTQxNTllMGIyMDJhMzUwNDEyZThlN2I=",
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
                                "id": "QXJ0d29yazo1ZDVjZmZjYjAyZTcyZjAwMTE2YWM3NTM=",
                                "slug": "egon-schiele-portrait-of-a-woman-1",
                                "href": "/artwork/egon-schiele-portrait-of-a-woman-1",
                                "internalID": "5d5cffcb02e72f00116ac753",
                                "image": {
                                   "aspect_ratio": 0.64,
                                   "placeholder": "155.57437200112898%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/dEfGhyjSZS2ex-lXuC6HrA/large.jpg"
                                },
                                "title": "Portrait of a Woman",
                                "image_title": "Egon Schiele, ‘Portrait of a Woman’, 1910",
                                "date": "1910",
                                "sale_message": "Sold",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRkOGI5MjgzNGViNjhhMWIyYzAwMDFhMA==",
                                      "href": "/artist/egon-schiele",
                                      "name": "Egon Schiele"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Galerie Kovacek & Zetter",
                                   "href": "/galerie-kovacek-and-zetter",
                                   "id": "UGFydG5lcjo1YTU2NDdkNWIyMDJhMzUxNzFjZmQ3NGE=",
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
                                "id": "QXJ0d29yazo1MTVkNmY2ZDVlZWIxYzUyNGMwMDRiNjg=",
                                "slug": "henri-de-toulouse-lautrec-mme-le-marguoin-milliner-mme-le-marguoin-modiste",
                                "href": "/artwork/henri-de-toulouse-lautrec-mme-le-marguoin-milliner-mme-le-marguoin-modiste",
                                "internalID": "515d6f6d5eeb1c524c004b68",
                                "image": {
                                   "aspect_ratio": 0.76,
                                   "placeholder": "132.15859030837004%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/n9NZ4P-0ZnbrACymAK2Vqg/large.jpg"
                                },
                                "title": "Mme. Le Marguoin, Milliner  (Mme. Le Marguoin, modiste)",
                                "image_title": "Henri de Toulouse-Lautrec, ‘Mme. Le Marguoin, Milliner  (Mme. Le Marguoin, modiste)’, 1900",
                                "date": "1900",
                                "sale_message": "Permanent collection",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRlZGY5Yjg4OTAxOTJiMDAwMTAwMTc4OQ==",
                                      "href": "/artist/henri-de-toulouse-lautrec",
                                      "name": "Henri de Toulouse-Lautrec"
                                   }
                                ],
                                "collecting_institution": "National Gallery of Art, Washington D.C.",
                                "partner": {
                                   "name": "National Gallery of Art, Washington, D.C.",
                                   "href": "/ngadc",
                                   "id": "UGFydG5lcjo0Zjk5YzdiNzkzYWI0YjAwMDEwMDAxNzk=",
                                   "type": "Institution"
                                },
                                "sale": None,
                                "sale_artwork": None,
                                "is_inquireable": False,
                                "is_saved": False,
                                "is_biddable": False
                             }
                          },
                          {
                             "__typename": "ArtworkEdge",
                             "node": {
                                "id": "QXJ0d29yazo1ZTg0Yjc4M2M1NGQxYzAwMTJmZDU4ODg=",
                                "slug": "odilon-redon-planche-dessai-no-1-femme-au-hennin",
                                "href": "/artwork/odilon-redon-planche-dessai-no-1-femme-au-hennin",
                                "internalID": "5e84b783c54d1c0012fd5888",
                                "image": {
                                   "aspect_ratio": 0.79,
                                   "placeholder": "126.87000726216414%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/X3HxYWT-Uykus_ioeaCOBw/large.jpg"
                                },
                                "title": "Planche d'Essai No. 1: Femme au Hennin",
                                "image_title": "Odilon Redon, ‘Planche d'Essai No. 1: Femme au Hennin’, 1900",
                                "date": "1900",
                                "sale_message": "$3,000",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjRlZTY4YzdlNmIxN2NmMDAwMTAwMjRkMA==",
                                      "href": "/artist/odilon-redon",
                                      "name": "Odilon Redon"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Childs Gallery",
                                   "href": "/childs-gallery",
                                   "id": "UGFydG5lcjo1MjI2Njk1NmViYWQ2NGQ0YTYwMDAwNWI=",
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
                                "id": "QXJ0d29yazo1Yjg2ZTZiYjczZDY3NDAwMmEyZjY0NjA=",
                                "slug": "jules-cheret-grand-theatre-of-the-fair-plate-221",
                                "href": "/artwork/jules-cheret-grand-theatre-of-the-fair-plate-221",
                                "internalID": "5b86e6bb73d674002a2f6460",
                                "image": {
                                   "aspect_ratio": 0.69,
                                   "placeholder": "144.92753623188406%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/L7BmWiQbPyNgBUPcwxk24Q/large.jpg"
                                },
                                "title": "Grand Theatre of the Fair (Plate 221)",
                                "image_title": "Jules Chéret, ‘Grand Theatre of the Fair (Plate 221)’, 1900",
                                "date": "1900",
                                "sale_message": "$995",
                                "cultural_maker": None,
                                "artists": [
                                   {
                                      "id": "QXJ0aXN0OjUxNWIwN2E3MjIzYWZhN2VhODAwMDE4MQ==",
                                      "href": "/artist/jules-cheret",
                                      "name": "Jules Chéret"
                                   }
                                ],
                                "collecting_institution": None,
                                "partner": {
                                   "name": "Martin Lawrence Galleries",
                                   "href": "/martin-lawrence-galleries",
                                   "id": "UGFydG5lcjo1YWEyZTkxZjhiM2I4MTdiMTZhNmQ4NjE=",
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
                                "id": "QXJ0d29yazo1Y2U0MmE5Yjg2ZTRlOTFjNDA3NzA4NzQ=",
                                "slug": "pablo-picasso-arlequin-moustachu-a-la-guitare-1",
                                "href": "/artwork/pablo-picasso-arlequin-moustachu-a-la-guitare-1",
                                "internalID": "5ce42a9b86e4e91c40770874",
                                "image": {
                                   "aspect_ratio": 0.79,
                                   "placeholder": "126%",
                                   "url": "https://d32dm0rphc51dk.cloudfront.net/3PMtIHQSt9_5K8X5yzs8BA/large.jpg"
                                },
                                "title": "Arlequin Moustachu a la Guitare",
                                "image_title": "Pablo Picasso, ‘Arlequin Moustachu a la Guitare’, 1973 original created in 1916",
                                "date": "1973 original created in 1916",
                                "sale_message": "$3,600",
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
                                   "name": "RoGallery",
                                   "href": "/rogallery",
                                   "id": "UGFydG5lcjo1NzBiZjRhNmNkNTMwZTY1OTEwMDBhYzQ=",
                                   "type": "Gallery"
                                },
                                "sale": None,
                                "sale_artwork": None,
                                "is_inquireable": False,
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
                             "id": "QXJ0d29yazo1MjVkN2RiMjljMThkYjY2YzUwMDA2YWU=",
                             "slug": "pierre-auguste-renoir-claude-renoir-tourne-a-gauche",
                             "href": "/artwork/pierre-auguste-renoir-claude-renoir-tourne-a-gauche",
                             "internalID": "525d7db29c18db66c50006ae",
                             "image": {
                                "aspect_ratio": 0.84,
                                "placeholder": "119.65811965811966%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/_TNO-d0fxLDqPZbSNU6VIg/large.jpg"
                             },
                             "title": "Claude Renoir, Tourne a Gauche",
                             "image_title": "Pierre-Auguste Renoir, ‘Claude Renoir, Tourne a Gauche’, ca. 1904",
                             "date": "ca. 1904",
                             "sale_message": "Contact For Price",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjljNGViNjhhMWIyYzAwMDJlMA==",
                                   "href": "/artist/pierre-auguste-renoir",
                                   "name": "Pierre-Auguste Renoir"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Contessa Gallery",
                                "href": "/contessa-gallery",
                                "id": "UGFydG5lcjo1MjRiNDRhNjljMThkYjllZmEwMDAwZjI=",
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
                             "id": "QXJ0d29yazo1OGY3ZWYzNzI3NWIyNDAzY2Q1MDU0Zjc=",
                             "slug": "henri-matisse-visage-legerement-penche-vers-la-gauche-8",
                             "href": "/artwork/henri-matisse-visage-legerement-penche-vers-la-gauche-8",
                             "internalID": "58f7ef37275b2403cd5054f7",
                             "image": {
                                "aspect_ratio": 0.66,
                                "placeholder": "152.0190023752969%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/RRa4bmBuDuW-srVcciKAkg/large.jpg"
                             },
                             "title": "Visage Légèrement Penché vers la Gauche",
                             "image_title": "Henri Matisse, ‘Visage Légèrement Penché vers la Gauche’, 1913",
                             "date": "1913",
                             "sale_message": "Contact For Price",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjkzNGViNjhhMWIyYzAwMDI1YQ==",
                                   "href": "/artist/henri-matisse",
                                   "name": "Henri Matisse"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie Maximillian",
                                "href": "/galerie-maximillian",
                                "id": "UGFydG5lcjo1MmZhNDZjNWM5ZGMyNDcxNzcwMDAxNzM=",
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
                             "id": "QXJ0d29yazo1YTc4YjE4MTJhODkzYTYwNzllN2M4YjU=",
                             "slug": "alfred-kubin-der-beste-arzt",
                             "href": "/artwork/alfred-kubin-der-beste-arzt",
                             "internalID": "5a78b1812a893a6079e7c8b5",
                             "image": {
                                "aspect_ratio": 1.33,
                                "placeholder": "75%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/uXKNQamSIurz5QuKOVR2HQ/large.jpg"
                             },
                             "title": "Der Beste Arzt",
                             "image_title": "Alfred Kubin, ‘Der Beste Arzt’, 1900-1909",
                             "date": "1900-1909",
                             "sale_message": "Sold",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjUwNmIzYTBjN2VkYzg5MDAwMjAwMGRhZA==",
                                   "href": "/artist/alfred-kubin",
                                   "name": "Alfred Kubin"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Lions Gallery",
                                "href": "/lions-gallery",
                                "id": "UGFydG5lcjo1YTQxNTllMGIyMDJhMzUwNDEyZThlN2I=",
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
                             "id": "QXJ0d29yazo1ZDVjZmZjYjAyZTcyZjAwMTE2YWM3NTM=",
                             "slug": "egon-schiele-portrait-of-a-woman-1",
                             "href": "/artwork/egon-schiele-portrait-of-a-woman-1",
                             "internalID": "5d5cffcb02e72f00116ac753",
                             "image": {
                                "aspect_ratio": 0.64,
                                "placeholder": "155.57437200112898%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/dEfGhyjSZS2ex-lXuC6HrA/large.jpg"
                             },
                             "title": "Portrait of a Woman",
                             "image_title": "Egon Schiele, ‘Portrait of a Woman’, 1910",
                             "date": "1910",
                             "sale_message": "Sold",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjgzNGViNjhhMWIyYzAwMDFhMA==",
                                   "href": "/artist/egon-schiele",
                                   "name": "Egon Schiele"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie Kovacek & Zetter",
                                "href": "/galerie-kovacek-and-zetter",
                                "id": "UGFydG5lcjo1YTU2NDdkNWIyMDJhMzUxNzFjZmQ3NGE=",
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
                             "id": "QXJ0d29yazo1MTVkNmY2ZDVlZWIxYzUyNGMwMDRiNjg=",
                             "slug": "henri-de-toulouse-lautrec-mme-le-marguoin-milliner-mme-le-marguoin-modiste",
                             "href": "/artwork/henri-de-toulouse-lautrec-mme-le-marguoin-milliner-mme-le-marguoin-modiste",
                             "internalID": "515d6f6d5eeb1c524c004b68",
                             "image": {
                                "aspect_ratio": 0.76,
                                "placeholder": "132.15859030837004%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/n9NZ4P-0ZnbrACymAK2Vqg/large.jpg"
                             },
                             "title": "Mme. Le Marguoin, Milliner  (Mme. Le Marguoin, modiste)",
                             "image_title": "Henri de Toulouse-Lautrec, ‘Mme. Le Marguoin, Milliner  (Mme. Le Marguoin, modiste)’, 1900",
                             "date": "1900",
                             "sale_message": "Permanent collection",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRlZGY5Yjg4OTAxOTJiMDAwMTAwMTc4OQ==",
                                   "href": "/artist/henri-de-toulouse-lautrec",
                                   "name": "Henri de Toulouse-Lautrec"
                                }
                             ],
                             "collecting_institution": "National Gallery of Art, Washington D.C.",
                             "partner": {
                                "name": "National Gallery of Art, Washington, D.C.",
                                "href": "/ngadc",
                                "id": "UGFydG5lcjo0Zjk5YzdiNzkzYWI0YjAwMDEwMDAxNzk=",
                                "type": "Institution"
                             },
                             "sale": None,
                             "sale_artwork": None,
                             "is_inquireable": False,
                             "is_saved": False,
                             "is_biddable": False
                          }
                       },
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1ZTg0Yjc4M2M1NGQxYzAwMTJmZDU4ODg=",
                             "slug": "odilon-redon-planche-dessai-no-1-femme-au-hennin",
                             "href": "/artwork/odilon-redon-planche-dessai-no-1-femme-au-hennin",
                             "internalID": "5e84b783c54d1c0012fd5888",
                             "image": {
                                "aspect_ratio": 0.79,
                                "placeholder": "126.87000726216414%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/X3HxYWT-Uykus_ioeaCOBw/large.jpg"
                             },
                             "title": "Planche d'Essai No. 1: Femme au Hennin",
                             "image_title": "Odilon Redon, ‘Planche d'Essai No. 1: Femme au Hennin’, 1900",
                             "date": "1900",
                             "sale_message": "$3,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRlZTY4YzdlNmIxN2NmMDAwMTAwMjRkMA==",
                                   "href": "/artist/odilon-redon",
                                   "name": "Odilon Redon"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Childs Gallery",
                                "href": "/childs-gallery",
                                "id": "UGFydG5lcjo1MjI2Njk1NmViYWQ2NGQ0YTYwMDAwNWI=",
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
                             "id": "QXJ0d29yazo1Yjg2ZTZiYjczZDY3NDAwMmEyZjY0NjA=",
                             "slug": "jules-cheret-grand-theatre-of-the-fair-plate-221",
                             "href": "/artwork/jules-cheret-grand-theatre-of-the-fair-plate-221",
                             "internalID": "5b86e6bb73d674002a2f6460",
                             "image": {
                                "aspect_ratio": 0.69,
                                "placeholder": "144.92753623188406%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/L7BmWiQbPyNgBUPcwxk24Q/large.jpg"
                             },
                             "title": "Grand Theatre of the Fair (Plate 221)",
                             "image_title": "Jules Chéret, ‘Grand Theatre of the Fair (Plate 221)’, 1900",
                             "date": "1900",
                             "sale_message": "$995",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjUxNWIwN2E3MjIzYWZhN2VhODAwMDE4MQ==",
                                   "href": "/artist/jules-cheret",
                                   "name": "Jules Chéret"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Martin Lawrence Galleries",
                                "href": "/martin-lawrence-galleries",
                                "id": "UGFydG5lcjo1YWEyZTkxZjhiM2I4MTdiMTZhNmQ4NjE=",
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
                             "id": "QXJ0d29yazo1Y2U0MmE5Yjg2ZTRlOTFjNDA3NzA4NzQ=",
                             "slug": "pablo-picasso-arlequin-moustachu-a-la-guitare-1",
                             "href": "/artwork/pablo-picasso-arlequin-moustachu-a-la-guitare-1",
                             "internalID": "5ce42a9b86e4e91c40770874",
                             "image": {
                                "aspect_ratio": 0.79,
                                "placeholder": "126%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/3PMtIHQSt9_5K8X5yzs8BA/large.jpg"
                             },
                             "title": "Arlequin Moustachu a la Guitare",
                             "image_title": "Pablo Picasso, ‘Arlequin Moustachu a la Guitare’, 1973 original created in 1916",
                             "date": "1973 original created in 1916",
                             "sale_message": "$3,600",
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
                                "name": "RoGallery",
                                "href": "/rogallery",
                                "id": "UGFydG5lcjo1NzBiZjRhNmNkNTMwZTY1OTEwMDBhYzQ=",
                                "type": "Gallery"
                             },
                             "sale": None,
                             "sale_artwork": None,
                             "is_inquireable": False,
                             "is_saved": False,
                             "is_biddable": False
                          }
                       }
                    ]
                 },
                 "id": "QXJ0d29ya0xheWVyOm1haW4="
              },
              "artistSeriesConnection": {
                 "edges": [
                    {
                       "node": {
                          "slug": "alphonse-mucha-job",
                          "internalID": "761c5d7a-85cc-44f0-9d27-213eab4fe3aa",
                          "filterArtworksConnection": {
                             "edges": [
                                {
                                   "node": {
                                      "slug": "alphonse-mucha-job-31",
                                      "internalID": "5f5a351cb6ff97000fdeabe8",
                                      "image": {
                                         "url": "https://d32dm0rphc51dk.cloudfront.net/e6JEFiTAconIQV5607fbww/large.jpg",
                                         "aspectRatio": 0.73
                                      },
                                      "imageTitle": "Alphonse Mucha, ‘Job’, 1899",
                                      "title": "Job",
                                      "href": "/artwork/alphonse-mucha-job-31",
                                      "date": "1899",
                                      "sale_message": "Sold",
                                      "cultural_maker": None,
                                      "artists": [
                                         {
                                            "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                            "href": "/artist/alphonse-mucha",
                                            "name": "Alphonse Mucha"
                                         }
                                      ],
                                      "collecting_institution": None,
                                      "partner": {
                                         "name": "NCAG",
                                         "href": "/ncag",
                                         "id": "UGFydG5lcjo1YmZkN2ZjNTM4NTQwMjRmMjljMjJmNzM=",
                                         "type": "Gallery"
                                      },
                                      "sale": None,
                                      "sale_artwork": None,
                                      "is_inquireable": False,
                                      "id": "QXJ0d29yazo1ZjVhMzUxY2I2ZmY5NzAwMGZkZWFiZTg=",
                                      "is_saved": False,
                                      "is_biddable": False
                                   }
                                },
                                {
                                   "node": {
                                      "slug": "alphonse-mucha-job-32",
                                      "internalID": "5fad8605ef6b3200125d1c42",
                                      "image": {
                                         "url": "https://d32dm0rphc51dk.cloudfront.net/nyLdNZBbnQq5UL3usk5bjA/large.jpg",
                                         "aspectRatio": 0.76
                                      },
                                      "imageTitle": "Alphonse Mucha, ‘Job’, 1896",
                                      "title": "Job",
                                      "href": "/artwork/alphonse-mucha-job-32",
                                      "date": "1896",
                                      "sale_message": None,
                                      "cultural_maker": None,
                                      "artists": [
                                         {
                                            "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                            "href": "/artist/alphonse-mucha",
                                            "name": "Alphonse Mucha"
                                         }
                                      ],
                                      "collecting_institution": None,
                                      "partner": {
                                         "name": "Hindman",
                                         "href": "/auction/leslie-hindman-auctioneers",
                                         "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                         "type": "Auction House"
                                      },
                                      "sale": {
                                         "is_auction": True,
                                         "is_closed": True,
                                         "id": "U2FsZTo1ZmFkN2UyNGM1M2ExYjAwMTI4ZDA5ODY=",
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
                                            "display": "$5,000"
                                         },
                                         "id": "U2FsZUFydHdvcms6NWZhZDg2MDcyYjA4OTgwMDEyNWVjNjlm"
                                      },
                                      "is_inquireable": False,
                                      "id": "QXJ0d29yazo1ZmFkODYwNWVmNmIzMjAwMTI1ZDFjNDI=",
                                      "is_saved": False,
                                      "is_biddable": False
                                   }
                                },
                                {
                                   "node": {
                                      "slug": "alphonse-mucha-job-16",
                                      "internalID": "5c1bc8da1310911d6b00283e",
                                      "image": {
                                         "url": "https://d32dm0rphc51dk.cloudfront.net/SOg40ztkfIqgOTElXASkiA/large.jpg",
                                         "aspectRatio": 0.69
                                      },
                                      "imageTitle": "Alphonse Mucha, ‘Job’, 1896",
                                      "title": "Job",
                                      "href": "/artwork/alphonse-mucha-job-16",
                                      "date": "1896",
                                      "sale_message": None,
                                      "cultural_maker": None,
                                      "artists": [
                                         {
                                            "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                            "href": "/artist/alphonse-mucha",
                                            "name": "Alphonse Mucha"
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
                                         "id": "U2FsZTo1YzFhNzYwNDhiYTJiNjYxMDlhYWYzNTk=",
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
                                            "display": "£7,000"
                                         },
                                         "id": "U2FsZUFydHdvcms6NWMxYmM4ZGJjNTE2MzM1ZmFmMzhjNjM4"
                                      },
                                      "is_inquireable": False,
                                      "id": "QXJ0d29yazo1YzFiYzhkYTEzMTA5MTFkNmIwMDI4M2U=",
                                      "is_saved": False,
                                      "is_biddable": False
                                   }
                                },
                                {
                                   "node": {
                                      "slug": "alphonse-mucha-job-21",
                                      "internalID": "5d9630bb5ff339001376560b",
                                      "image": {
                                         "url": "https://d32dm0rphc51dk.cloudfront.net/eLndsQDFY_lb6FkaAkt7nA/large.jpg",
                                         "aspectRatio": 0.65
                                      },
                                      "imageTitle": "Alphonse Mucha, ‘Job’, 1898",
                                      "title": "Job",
                                      "href": "/artwork/alphonse-mucha-job-21",
                                      "date": "1898",
                                      "sale_message": None,
                                      "cultural_maker": None,
                                      "artists": [
                                         {
                                            "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                            "href": "/artist/alphonse-mucha",
                                            "name": "Alphonse Mucha"
                                         }
                                      ],
                                      "collecting_institution": None,
                                      "partner": {
                                         "name": "Isselbacher Gallery",
                                         "href": "/isselbacher-gallery",
                                         "id": "UGFydG5lcjo1OTc5MDFmY2FiNjBjYTYwZDI0NmNmZTE=",
                                         "type": "Gallery"
                                      },
                                      "sale": None,
                                      "sale_artwork": None,
                                      "is_inquireable": False,
                                      "id": "QXJ0d29yazo1ZDk2MzBiYjVmZjMzOTAwMTM3NjU2MGI=",
                                      "is_saved": False,
                                      "is_biddable": False
                                   }
                                },
                                {
                                   "node": {
                                      "slug": "alphonse-mucha-job-15",
                                      "internalID": "5bc131970ac6a60345d21230",
                                      "image": {
                                         "url": "https://d32dm0rphc51dk.cloudfront.net/lN_lSsTft4tw442DvmTTjg/large.jpg",
                                         "aspectRatio": 0.67
                                      },
                                      "imageTitle": "Alphonse Mucha, ‘Job’, 1898",
                                      "title": "Job",
                                      "href": "/artwork/alphonse-mucha-job-15",
                                      "date": "1898",
                                      "sale_message": None,
                                      "cultural_maker": None,
                                      "artists": [
                                         {
                                            "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                            "href": "/artist/alphonse-mucha",
                                            "name": "Alphonse Mucha"
                                         }
                                      ],
                                      "collecting_institution": None,
                                      "partner": {
                                         "name": "Christie's",
                                         "href": "/auction/partner-553e693d7261695a85350100",
                                         "id": "UGFydG5lcjo1NTNlNjkzZDcyNjE2OTVhODUzNTAxMDA=",
                                         "type": "Auction House"
                                      },
                                      "sale": {
                                         "is_auction": True,
                                         "is_closed": True,
                                         "id": "U2FsZTo1YmJhYWVmYTZlOTY0ZDE4MmY3ZDQzMDA=",
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
                                            "display": "$4,800"
                                         },
                                         "id": "U2FsZUFydHdvcms6NWJjMTMxOTkwYWYwM2M3NDRiOTFlNTMy"
                                      },
                                      "is_inquireable": False,
                                      "id": "QXJ0d29yazo1YmMxMzE5NzBhYzZhNjAzNDVkMjEyMzA=",
                                      "is_saved": False,
                                      "is_biddable": False
                                   }
                                },
                                {
                                   "node": {
                                      "slug": "alphonse-mucha-job-22",
                                      "internalID": "5ddd55d152539a000ef8c6d3",
                                      "image": {
                                         "url": "https://d32dm0rphc51dk.cloudfront.net/nP1YQtAICPd8B5Hyt_L-7w/large.jpg",
                                         "aspectRatio": 0.67
                                      },
                                      "imageTitle": "Alphonse Mucha, ‘Job’, 1898",
                                      "title": "Job",
                                      "href": "/artwork/alphonse-mucha-job-22",
                                      "date": "1898",
                                      "sale_message": None,
                                      "cultural_maker": None,
                                      "artists": [
                                         {
                                            "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                            "href": "/artist/alphonse-mucha",
                                            "name": "Alphonse Mucha"
                                         }
                                      ],
                                      "collecting_institution": None,
                                      "partner": {
                                         "name": "Hindman",
                                         "href": "/auction/leslie-hindman-auctioneers",
                                         "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                         "type": "Auction House"
                                      },
                                      "sale": {
                                         "is_auction": True,
                                         "is_closed": True,
                                         "id": "U2FsZTo1ZGQ4MmQyM2UwYTdkYzAwMTI5ZThhM2E=",
                                         "is_live_open": False,
                                         "is_open": False,
                                         "is_preview": False,
                                         "display_timely_at": None
                                      },
                                      "sale_artwork": {
                                         "counts": {
                                            "bidder_positions": 1
                                         },
                                         "highest_bid": {
                                            "display": "$1,500"
                                         },
                                         "opening_bid": {
                                            "display": "$1,500"
                                         },
                                         "id": "U2FsZUFydHdvcms6NWRkZDU1ZDg2NGVlM2YwMDBlM2JjZTkz"
                                      },
                                      "is_inquireable": False,
                                      "id": "QXJ0d29yazo1ZGRkNTVkMTUyNTM5YTAwMGVmOGM2ZDM=",
                                      "is_saved": False,
                                      "is_biddable": False
                                   }
                                },
                                {
                                   "node": {
                                      "slug": "alphonse-mucha-job-r-dot-slash-w-51",
                                      "internalID": "5ad62fd01a1e861674647987",
                                      "image": {
                                         "url": "https://d32dm0rphc51dk.cloudfront.net/j6DhgDcFZVX64bS-d_YwQA/large.jpg",
                                         "aspectRatio": 0.66
                                      },
                                      "imageTitle": "Alphonse Mucha, ‘Job (R./W. 51)’, 1898",
                                      "title": "Job (R./W. 51)",
                                      "href": "/artwork/alphonse-mucha-job-r-dot-slash-w-51",
                                      "date": "1898",
                                      "sale_message": None,
                                      "cultural_maker": None,
                                      "artists": [
                                         {
                                            "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                            "href": "/artist/alphonse-mucha",
                                            "name": "Alphonse Mucha"
                                         }
                                      ],
                                      "collecting_institution": None,
                                      "partner": {
                                         "name": "Doyle",
                                         "href": "/auction/partner-595e64cdcd530e765d529647",
                                         "id": "UGFydG5lcjo1OTVlNjRjZGNkNTMwZTc2NWQ1Mjk2NDc=",
                                         "type": "Auction House"
                                      },
                                      "sale": {
                                         "is_auction": True,
                                         "is_closed": True,
                                         "id": "U2FsZTo1YWQwZTAzYWNiNGMyNzE4NDdhNmYwY2E=",
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
                                            "display": "$1,500"
                                         },
                                         "id": "U2FsZUFydHdvcms6NWFkNjJmZDJjYjRjMjcxNDFlNWE1MmQw"
                                      },
                                      "is_inquireable": False,
                                      "id": "QXJ0d29yazo1YWQ2MmZkMDFhMWU4NjE2NzQ2NDc5ODc=",
                                      "is_saved": False,
                                      "is_biddable": False
                                   }
                                },
                                {
                                   "node": {
                                      "slug": "alphonse-mucha-job-poster-from-maxims-chicago",
                                      "internalID": "5a625795cd530e51721f2193",
                                      "image": {
                                         "url": "https://d32dm0rphc51dk.cloudfront.net/qhcaHomPZ6bTSE3YAEz2cw/large.jpg",
                                         "aspectRatio": 1
                                      },
                                      "imageTitle": "Alphonse Mucha, ‘Job poster from Maxim's, Chicago’, 1898",
                                      "title": "Job poster from Maxim's, Chicago",
                                      "href": "/artwork/alphonse-mucha-job-poster-from-maxims-chicago",
                                      "date": "1898",
                                      "sale_message": None,
                                      "cultural_maker": None,
                                      "artists": [
                                         {
                                            "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                            "href": "/artist/alphonse-mucha",
                                            "name": "Alphonse Mucha"
                                         }
                                      ],
                                      "collecting_institution": None,
                                      "partner": {
                                         "name": "Rago/Wright",
                                         "href": "/auction/partner-595e69f6a09a671938435977",
                                         "id": "UGFydG5lcjo1OTVlNjlmNmEwOWE2NzE5Mzg0MzU5Nzc=",
                                         "type": "Auction House"
                                      },
                                      "sale": {
                                         "is_auction": True,
                                         "is_closed": True,
                                         "id": "U2FsZTo1YTYyMzE2ZDljMThkYjdiYTgyZDRiOWE=",
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
                                            "display": "$2,800"
                                         },
                                         "opening_bid": {
                                            "display": "$2,200"
                                         },
                                         "id": "U2FsZUFydHdvcms6NWE2MjU3OTdhMDlhNjcxNWZkNjM1MTFm"
                                      },
                                      "is_inquireable": False,
                                      "id": "QXJ0d29yazo1YTYyNTc5NWNkNTMwZTUxNzIxZjIxOTM=",
                                      "is_saved": False,
                                      "is_biddable": False
                                   }
                                }
                             ],
                             "id": "ZmlsdGVyQXJ0d29ya3NDb25uZWN0aW9uOnsiYWdncmVnYXRpb25zIjpbInRvdGFsIl0sImFydGlzdF9zZXJpZXNfaWQiOiI3NjFjNWQ3YS04NWNjLTQ0ZjAtOWQyNy0yMTNlYWI0ZmUzYWEiLCJleGNsdWRlX2FydHdvcmtfaWRzIjpbIjVjYWJhMDk4ODc3NDg5NDFlZTdiMWRlMCJdLCJwYWdlIjoxLCJzaXplIjoyMCwic29ydCI6Ii1kZWNheWVkX21lcmNoIn0="
                          }
                       }
                    }
                 ]
              },
              "seriesArtist": {
                 "artistSeriesConnection": {
                    "edges": [
                       {
                          "node": {
                             "internalID": "f312bae3-f9d0-4259-871f-a0d4599a3f55",
                             "title": "Lorenzaccio",
                             "slug": "alphonse-mucha-lorenzaccio",
                             "featured": False,
                             "artworksCountMessage": "2 available",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FH-x6cmA8HIiTQO9JTR51NA%2Flarge.jpg"
                                }
                             }
                          }
                       },
                       {
                          "node": {
                             "internalID": "cb81251b-b90d-4f14-9b8c-33b1131daadb",
                             "title": "Moët & Chandon",
                             "slug": "alphonse-mucha-moet-and-chandon",
                             "featured": False,
                             "artworksCountMessage": "2 available",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FCBrNJiuuneh_Zm_TdIc6Yg%2Flarge.jpg"
                                }
                             }
                          }
                       },
                       {
                          "node": {
                             "internalID": "3c7388ef-d425-4077-92f6-64f7f21524b5",
                             "title": "Salon des Cents",
                             "slug": "alphonse-mucha-salon-des-cents",
                             "featured": False,
                             "artworksCountMessage": "2 available",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FzVERnQ3TkrYJcokNH6K3yA%2Flarge.jpg"
                                }
                             }
                          }
                       },
                       {
                          "node": {
                             "internalID": "27214b0a-a5da-426c-a8d7-9facf72b1487",
                             "title": "Seasons",
                             "slug": "alphonse-mucha-seasons",
                             "featured": False,
                             "artworksCountMessage": "2 available",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FMzMOn0ZxhKjaVkq54qQ8Hg%2Flarge.jpg"
                                }
                             }
                          }
                       },
                       {
                          "node": {
                             "internalID": "761c5d7a-85cc-44f0-9d27-213eab4fe3aa",
                             "title": "Job",
                             "slug": "alphonse-mucha-job",
                             "featured": False,
                             "artworksCountMessage": "1 available",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FeLndsQDFY_lb6FkaAkt7nA%2Flarge.jpg"
                                }
                             }
                          }
                       },
                       {
                          "node": {
                             "internalID": "8582d221-3b68-4173-a2bb-3e1980c53d0e",
                             "title": "Biscuits",
                             "slug": "alphonse-mucha-biscuits",
                             "featured": False,
                             "artworksCountMessage": "1 available",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FZROpbxzCrq8QhM0f6zx6qw%2Flarge.jpg"
                                }
                             }
                          }
                       }
                    ]
                 },
                 "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ=="
              },
              "seriesForCounts": {
                 "edges": [
                    {
                       "node": {
                          "artworksCount": 9
                       }
                    }
                 ]
              },
              "pricingContext": {
                 "appliedFiltersDisplay": "Price ranges of small prints by Alphonse Mucha",
                 "appliedFilters": {
                    "dimension": "SMALL",
                    "category": "PRINT"
                 },
                 "bins": [
                    {
                       "maxPrice": "$1,050",
                       "maxPriceCents": 105000,
                       "minPrice": "$700",
                       "minPriceCents": 70000,
                       "numArtworks": 3
                    },
                    {
                       "maxPrice": "$1,400",
                       "maxPriceCents": 140000,
                       "minPrice": "$1,050",
                       "minPriceCents": 105000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$1,750",
                       "maxPriceCents": 175000,
                       "minPrice": "$1,400",
                       "minPriceCents": 140000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$2,100",
                       "maxPriceCents": 210000,
                       "minPrice": "$1,750",
                       "minPriceCents": 175000,
                       "numArtworks": 1
                    },
                    {
                       "maxPrice": "$2,450",
                       "maxPriceCents": 245000,
                       "minPrice": "$2,100",
                       "minPriceCents": 210000,
                       "numArtworks": 1
                    },
                    {
                       "maxPrice": "$2,800",
                       "maxPriceCents": 280000,
                       "minPrice": "$2,450",
                       "minPriceCents": 245000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$3,150",
                       "maxPriceCents": 315000,
                       "minPrice": "$2,800",
                       "minPriceCents": 280000,
                       "numArtworks": 4
                    },
                    {
                       "maxPrice": "$3,500",
                       "maxPriceCents": 350000,
                       "minPrice": "$3,150",
                       "minPriceCents": 315000,
                       "numArtworks": 1
                    },
                    {
                       "maxPrice": "$3,850",
                       "maxPriceCents": 385000,
                       "minPrice": "$3,500",
                       "minPriceCents": 350000,
                       "numArtworks": 3
                    },
                    {
                       "maxPrice": "$4,200",
                       "maxPriceCents": 420000,
                       "minPrice": "$3,850",
                       "minPriceCents": 385000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$4,550",
                       "maxPriceCents": 455000,
                       "minPrice": "$4,200",
                       "minPriceCents": 420000,
                       "numArtworks": 1
                    },
                    {
                       "maxPrice": "$4,900",
                       "maxPriceCents": 490000,
                       "minPrice": "$4,550",
                       "minPriceCents": 455000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$5,250",
                       "maxPriceCents": 525000,
                       "minPrice": "$4,900",
                       "minPriceCents": 490000,
                       "numArtworks": 4
                    },
                    {
                       "maxPrice": "$5,600",
                       "maxPriceCents": 560000,
                       "minPrice": "$5,250",
                       "minPriceCents": 525000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$5,950",
                       "maxPriceCents": 595000,
                       "minPrice": "$5,600",
                       "minPriceCents": 560000,
                       "numArtworks": 2
                    },
                    {
                       "maxPrice": "$6,300",
                       "maxPriceCents": 630000,
                       "minPrice": "$5,950",
                       "minPriceCents": 595000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$6,650",
                       "maxPriceCents": 665000,
                       "minPrice": "$6,300",
                       "minPriceCents": 630000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$7,000",
                       "maxPriceCents": 700000,
                       "minPrice": "$6,650",
                       "minPriceCents": 665000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$7,350",
                       "maxPriceCents": 735000,
                       "minPrice": "$7,000",
                       "minPriceCents": 700000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$7,700",
                       "maxPriceCents": 770000,
                       "minPrice": "$7,350",
                       "minPriceCents": 735000,
                       "numArtworks": 0
                    },
                    {
                       "maxPrice": "$8,050",
                       "maxPriceCents": 805000,
                       "minPrice": "$7,700",
                       "minPriceCents": 770000,
                       "numArtworks": 1
                    }
                 ]
              }
           },
           "me": None
        }
     },
     "data": {
        "artwork": {
           "slug": "alphonse-mucha-job-30",
           "internalID": "5caba09887748941ee7b1de0",
           "is_acquireable": False,
           "is_offerable": False,
           "availability": "for sale",
           "listPrice": {
              "__typename": "PriceRange",
              "display": "$10,000 - 15,000",
              "minPrice": {
                 "major": 10000,
                 "currencyCode": "USD",
                 "minor": 1000000
              },
              "maxPrice": {
                 "major": 15000,
                 "minor": 1500000
              }
           },
           "is_in_auction": False,
           "sale": None,
           "artists": [
              {
                 "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                 "slug": "alphonse-mucha",
                 "internalID": "4fbabc998b313700010006da",
                 "name": "Alphonse Mucha",
                 "href": "/artist/alphonse-mucha",
                 "image": {
                    "cropped": {
                       "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=100&height=100&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FPd_DniK14Fp7kZ4sO18fVQ%2Flarge.jpg"
                    }
                 },
                 "formatted_nationality_and_birthday": "Czech, 1860–1939",
                 "counts": {
                    "partner_shows": 24,
                    "follows": 2772
                 },
                 "exhibition_highlights": [
                    {
                       "partner": {
                          "__typename": "Partner",
                          "name": "David Barnett Gallery",
                          "id": "UGFydG5lcjo1YTVmOGNmZjhiM2I4MTQzZTU0OTJmM2I="
                       },
                       "name": "Alphonse Mucha: Art Nouveau",
                       "start_at": "2017",
                       "cover_image": {
                          "cropped": {
                             "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F9n3U-BmG7kIwBtZWHmMxPw%2Flarge.jpg"
                          }
                       },
                       "city": "Milwaukee",
                       "id": "U2hvdzo1YTZjY2YxMjJhODkzYTc4Mzk5Y2M1Y2Y="
                    },
                    {
                       "partner": {
                          "__typename": "Partner",
                          "name": "Rue Royale Fine Art",
                          "id": "UGFydG5lcjo1NDZmN2I5MzcyNjE2OTY2Y2ZlOTAxMDA="
                       },
                       "name": "Celestial Nymphs",
                       "start_at": "2014",
                       "cover_image": {
                          "cropped": {
                             "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fftwed6EP_b9STMNmDeTBsQ%2Flarge.jpg"
                          }
                       },
                       "city": "Las Vegas",
                       "id": "U2hvdzo1NGE3MzMzZTcyNjE2OTQyMmIxNjA4MDA="
                    },
                    {
                       "partner": {
                          "__typename": "Partner",
                          "name": "Larsen Gallery",
                          "id": "UGFydG5lcjo1OGRlZWFiZjJhODkzYTI1OGM2NjFlMTM="
                       },
                       "name": "2020 Fall Larsen Art Auction Post Auction Sale",
                       "start_at": "2020",
                       "cover_image": {
                          "cropped": {
                             "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FN3a4uZhlXrcVGZCzypAgDw%2Flarge.jpg"
                          }
                       },
                       "city": "Scottsdale",
                       "id": "U2hvdzo1Zjk3NjA2NTA3NmJhZTAwMTI0M2QyMzM="
                    }
                 ],
                 "collections": [
                    "Museum of Modern Art (MoMA)"
                 ],
                 "highlights": {
                    "partnersConnection": {
                       "edges": []
                    }
                 },
                 "auctionResultsConnection": None,
                 "biographyBlurb": {
                    "text": "<p>Alphonse Mucha is synonymous with <a href=\"/gene/art-nouveau\">Art Nouveau<\/a>, a style of fine art, decorative art, and architecture that broke with the academicism of the 19th century in favor of florid lines inspired by the natural environment. A lithographed advertising poster he was commissioned to create for a play featuring the celebrated actress Sarah Bernhardt in 1894 catapulted him out of obscurity and brought him instant success as a commercial artist. Rendered in pale pastels, much of his work depicts beautiful young women draped in Neoclassical robes set amidst flowers, feathers, and other sensuous natural forms. He was celebrated not only for illustrating advertising posters, but also for painting, book illustrations, sculpting, and designing theater sets, jewelry, and wallpaper. <\/p>\n"
                 },
                 "is_followed": False,
                 "related": {
                    "suggestedConnection": None
                 },
                 "is_consignable": True
              }
           ],
           "artist": {
              "internalID": "4fbabc998b313700010006da",
              "slug": "alphonse-mucha",
              "name": "Alphonse Mucha",
              "href": "/artist/alphonse-mucha",
              "image": {
                 "cropped": {
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=100&height=100&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FPd_DniK14Fp7kZ4sO18fVQ%2Flarge.jpg"
                 }
              },
              "formatted_nationality_and_birthday": "Czech, 1860–1939",
              "counts": {
                 "partner_shows": 24,
                 "follows": 2772
              },
              "exhibition_highlights": [
                 {
                    "partner": {
                       "__typename": "Partner",
                       "name": "David Barnett Gallery",
                       "id": "UGFydG5lcjo1YTVmOGNmZjhiM2I4MTQzZTU0OTJmM2I="
                    },
                    "name": "Alphonse Mucha: Art Nouveau",
                    "start_at": "2017",
                    "cover_image": {
                       "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F9n3U-BmG7kIwBtZWHmMxPw%2Flarge.jpg"
                       }
                    },
                    "city": "Milwaukee",
                    "id": "U2hvdzo1YTZjY2YxMjJhODkzYTc4Mzk5Y2M1Y2Y="
                 },
                 {
                    "partner": {
                       "__typename": "Partner",
                       "name": "Rue Royale Fine Art",
                       "id": "UGFydG5lcjo1NDZmN2I5MzcyNjE2OTY2Y2ZlOTAxMDA="
                    },
                    "name": "Celestial Nymphs",
                    "start_at": "2014",
                    "cover_image": {
                       "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fftwed6EP_b9STMNmDeTBsQ%2Flarge.jpg"
                       }
                    },
                    "city": "Las Vegas",
                    "id": "U2hvdzo1NGE3MzMzZTcyNjE2OTQyMmIxNjA4MDA="
                 },
                 {
                    "partner": {
                       "__typename": "Partner",
                       "name": "Larsen Gallery",
                       "id": "UGFydG5lcjo1OGRlZWFiZjJhODkzYTI1OGM2NjFlMTM="
                    },
                    "name": "2020 Fall Larsen Art Auction Post Auction Sale",
                    "start_at": "2020",
                    "cover_image": {
                       "cropped": {
                          "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=800&height=600&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FN3a4uZhlXrcVGZCzypAgDw%2Flarge.jpg"
                       }
                    },
                    "city": "Scottsdale",
                    "id": "U2hvdzo1Zjk3NjA2NTA3NmJhZTAwMTI0M2QyMzM="
                 }
              ],
              "collections": [
                 "Museum of Modern Art (MoMA)"
              ],
              "highlights": {
                 "partnersConnection": {
                    "edges": []
                 }
              },
              "auctionResultsConnection": None,
              "biographyBlurb": {
                 "text": "<p>Alphonse Mucha is synonymous with <a href=\"/gene/art-nouveau\">Art Nouveau<\/a>, a style of fine art, decorative art, and architecture that broke with the academicism of the 19th century in favor of florid lines inspired by the natural environment. A lithographed advertising poster he was commissioned to create for a play featuring the celebrated actress Sarah Bernhardt in 1894 catapulted him out of obscurity and brought him instant success as a commercial artist. Rendered in pale pastels, much of his work depicts beautiful young women draped in Neoclassical robes set amidst flowers, feathers, and other sensuous natural forms. He was celebrated not only for illustrating advertising posters, but also for painting, book illustrations, sculpting, and designing theater sets, jewelry, and wallpaper. <\/p>\n"
              },
              "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
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
                             "name": "A.M. Cassandre",
                             "slug": "am-cassandre",
                             "href": "/artist/am-cassandre",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FtahOUuHJ9BgRev8eBzlkTw%2Flarge.jpg"
                                }
                             },
                             "formatted_nationality_and_birthday": "French, 1901–1968",
                             "id": "QXJ0aXN0OjU5Mjc4OGYwMmE4OTNhMmE3NjFlMmM4Ng==",
                             "internalID": "592788f02a893a2a761e2c86",
                             "is_followed": False,
                             "counts": {
                                "follows": 201
                             },
                             "__typename": "Artist"
                          },
                          "cursor": "YXJyYXljb25uZWN0aW9uOjA="
                       },
                       {
                          "node": {
                             "name": "Henri-Gustave Jossot",
                             "slug": "henri-gustave-jossot",
                             "href": "/artist/henri-gustave-jossot",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FCyC6W7g7v1MYwMn4xuWpFw%2Flarge.jpg"
                                }
                             },
                             "formatted_nationality_and_birthday": "",
                             "id": "QXJ0aXN0OjU3NjAxMDJlNzYyMmRkNjVkZjAwMDI5Yw==",
                             "internalID": "5760102e7622dd65df00029c",
                             "is_followed": False,
                             "counts": {
                                "follows": 80
                             },
                             "__typename": "Artist"
                          },
                          "cursor": "YXJyYXljb25uZWN0aW9uOjE="
                       },
                       {
                          "node": {
                             "name": "Georges de Feure",
                             "slug": "georges-de-feure",
                             "href": "/artist/georges-de-feure",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FraDWU4JfDqepE0urJ6QUHQ%2Flarge.jpg"
                                }
                             },
                             "formatted_nationality_and_birthday": "French, 1868–1928",
                             "id": "QXJ0aXN0OjUyYTEwODAyMTM5YjIxYTY3ZTAwMDE5Mw==",
                             "internalID": "52a10802139b21a67e000193",
                             "is_followed": False,
                             "counts": {
                                "follows": 161
                             },
                             "__typename": "Artist"
                          },
                          "cursor": "YXJyYXljb25uZWN0aW9uOjI="
                       },
                       {
                          "node": {
                             "name": "Louis Abel-Truchet",
                             "slug": "louis-abel-truchet",
                             "href": "/artist/louis-abel-truchet",
                             "image": {
                                "cropped": {
                                   "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=400&height=300&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FwPAWlY-yXlp4_kNaGLT8_w%2Flarge.jpg"
                                }
                             },
                             "formatted_nationality_and_birthday": "French, 1857–1918",
                             "id": "QXJ0aXN0OjUyYTEwNzZiOGIzYjgxYzc0MjAwMDE5ZQ==",
                             "internalID": "52a1076b8b3b81c74200019e",
                             "is_followed": False,
                             "counts": {
                                "follows": 118
                             },
                             "__typename": "Artist"
                          },
                          "cursor": "YXJyYXljb25uZWN0aW9uOjM="
                       }
                    ]
                 }
              }
           },
           "href": "/artwork/alphonse-mucha-job-30",
           "date": "1900",
           "artist_names": "Alphonse Mucha",
           "sale_message": "$10,000 - 15,000",
           "partner": {
              "name": "Galerie d'Orsay",
              "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
              "type": "Gallery",
              "profile": {
                 "image": {
                    "resized": {
                       "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FxtN5t2O49vsCc07XP4wopQ%2Fwide.jpg"
                    }
                 },
                 "id": "UHJvZmlsZTo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmY=",
                 "slug": "galerie-dorsay",
                 "name": "Galerie d'Orsay",
                 "internalID": "557f1a92776f7260b20000ff",
                 "is_followed": False,
                 "icon": {
                    "url": "https://d32dm0rphc51dk.cloudfront.net/SjLYl9ZCWlfGZx2NCc4NKQ/square140.png"
                 }
              },
              "initials": "GO",
              "href": "/galerie-dorsay",
              "locations": [
                 {
                    "city": "Boston",
                    "id": "TG9jYXRpb246NTg3NjljMmVhMDlhNjczN2ZlMDAxMDEy"
                 }
              ],
              "isVerifiedSeller": False,
              "internalID": "557f1a92776f7260b20000fd",
              "slug": "galerie-dorsay",
              "is_default_profile_public": True
           },
           "image_rights": "",
           "is_shareable": True,
           "meta_image": {
              "resized": {
                 "width": 640,
                 "height": 824,
                 "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=640&height=824&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fz6cZrfbgQXCnoZPztYQTsQ%2Flarge.jpg"
              }
           },
           "meta": {
              "title": "Alphonse Mucha | Job (1900) | Available for Sale | Artsy",
              "description": "Available for sale from Galerie d'Orsay, Alphonse Mucha, Job (1900), Lithograph on wove paper, 11 1/2 × 8 7/8 in",
              "long_description": "Available for sale from Galerie d'Orsay, Alphonse Mucha, Job (1900), Lithograph on wove paper, 11 1/2 × 8 7/8 in"
           },
           "context": {
              "__typename": "Show",
              "id": "U2hvdzo1ZWMwNjBjNGFkNmQyOTAwMGVkNDY2MTQ=",
              "name": "Galerie d'Orsay: Celebrating Twenty Years & Counting!",
              "href": "/show/galerie-dorsay-galerie-dorsay-celebrating-twenty-years-and-counting",
              "status": "closed",
              "thumbnail": {
                 "img": {
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=70&height=70&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fd-Opl4tVJi1OHlBYzkhcNw%2Fsquare.jpg"
                 }
              }
           },
           "is_price_hidden": False,
           "is_price_range": True,
           "category": "Print",
           "dimensions": {
              "in": "11 1/2 × 8 7/8 in",
              "cm": "29.2 × 22.5 cm"
           },
           "cultural_maker": None,
           "is_biddable": False,
           "edition_sets": [],
           "sale_artwork": None,
           "title": "Job",
           "medium": "Lithograph on wove paper",
           "edition_of": None,
           "attributionClass": {
              "shortDescription": "This work is from an edition of unknown size",
              "id": "QXR0cmlidXRpb25DbGFzczp1bmtub3duIGVkaXRpb24="
           },
           "myLotStanding": None,
           "is_for_sale": True,
           "is_inquireable": True,
           "priceIncludesTaxDisplay": None,
           "shippingInfo": "Shipping, tax, and additional fees quoted by seller",
           "shippingOrigin": "Boston, MA, US",
           "hasCertificateOfAuthenticity": True,
           "description": None,
           "additional_information": None,
           "series": "Masters of the Poster",
           "publisher": "Published by Jules Chéret; printed at Impremiere Chaix (Atelier Chéret), Paris.",
           "manufacturer": None,
           "canRequestLotConditionsReport": False,
           "framed": {
              "label": "Framed",
              "details": "Included"
           },
           "signatureInfo": {
              "label": "Signature",
              "details": "Signed on the stone lower right Mucha"
           },
           "conditionDescription": {
              "label": "Condition details",
              "details": "In excellent condition, with bright, fresh colors, printed on a sheet with full margins."
           },
           "certificateOfAuthenticity": {
              "label": "Certificate of authenticity",
              "details": "Included"
           },
           "mediumType": {
              "__typename": "ArtworkMedium",
              "name": "Print",
              "longDescription": "Includes etchings; engravings; lithographs; monoprints; screen prints; woodcuts."
           },
           "articles": [],
           "literature": None,
           "exhibition_history": None,
           "provenance": None,
           "image_alt": "Alphonse Mucha, ‘Job’, 1900, Galerie d'Orsay",
           "id": "QXJ0d29yazo1Y2FiYTA5ODg3NzQ4OTQxZWU3YjFkZTA=",
           "is_saved": False,
           "images": [
              {
                 "url": "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/larger.jpg",
                 "internalID": "5caba09987748941ee7b1de6",
                 "uri": "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/large.jpg",
                 "placeholder": {
                    "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fit&width=30&height=38&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2Fz6cZrfbgQXCnoZPztYQTsQ%2Fsmall.jpg"
                 },
                 "aspectRatio": 0.78,
                 "is_zoomable": True,
                 "is_default": True,
                 "deepZoom": {
                    "Image": {
                       "xmlns": "http://schemas.microsoft.com/deepzoom/2008",
                       "Url": "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/dztiles/",
                       "Format": "jpg",
                       "TileSize": 512,
                       "Overlap": 0,
                       "Size": {
                          "Width": 1128,
                          "Height": 1454
                       }
                    }
                 }
              }
           ],
           "artworkMeta": {
              "share": "Check out Alphonse Mucha, Job (1900), From Galerie d'Orsay"
           },
           "image": {
              "internalID": "5caba09987748941ee7b1de6",
              "url": "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/larger.jpg",
              "height": 1454,
              "width": 1128
           },
           "is_downloadable": False,
           "is_hangable": True,
           "contextGrids": [
              {
                 "__typename": "ShowArtworkGrid",
                 "title": "Other works from Galerie d'Orsay: Celebrating Twenty Years & Counting!",
                 "ctaTitle": "View all works from the show",
                 "ctaHref": "/show/galerie-dorsay-galerie-dorsay-celebrating-twenty-years-and-counting",
                 "artworksConnection": {
                    "edges": [
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1ZWM1YTdlZDBhZDIyMDAwMGRiNWVmMmU=",
                             "slug": "pierre-auguste-renoir-lenfant-au-biscuit-jean-renoir-5",
                             "href": "/artwork/pierre-auguste-renoir-lenfant-au-biscuit-jean-renoir-5",
                             "internalID": "5ec5a7ed0ad220000db5ef2e",
                             "image": {
                                "aspect_ratio": 0.82,
                                "placeholder": "121.73913043478262%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/vSfSCiWOK7k3PLzOL5BVJQ/large.jpg"
                             },
                             "title": "L'Enfant au Biscuit (Jean Renoir)",
                             "image_title": "Pierre-Auguste Renoir, ‘L'Enfant au Biscuit (Jean Renoir)’, 1841-1919",
                             "date": "1841-1919",
                             "sale_message": "$30,000 - 40,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjljNGViNjhhMWIyYzAwMDJlMA==",
                                   "href": "/artist/pierre-auguste-renoir",
                                   "name": "Pierre-Auguste Renoir"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ODgzOWJkYzc2MjJkZDExOTgwMDAxNzA=",
                             "slug": "edouard-manet-jeanne-le-printemps",
                             "href": "/artwork/edouard-manet-jeanne-le-printemps",
                             "internalID": "58839bdc7622dd1198000170",
                             "image": {
                                "aspect_ratio": 0.8,
                                "placeholder": "125.7510729613734%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/ebElhRb46RXI3WgRzPryVQ/large.jpg"
                             },
                             "title": "Jeanne (Le Printemps)",
                             "image_title": "Édouard Manet, ‘Jeanne (Le Printemps)’, 1882",
                             "date": "1882",
                             "sale_message": "$7,500 - 10,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjdlNGViNjhhMWIyYzAwMDE2OA==",
                                   "href": "/artist/edouard-manet",
                                   "name": "Édouard Manet"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZWM1YTI5ZDRhOGMzNDAwMGVmMDMxOTY=",
                             "slug": "georges-rouault-parade",
                             "href": "/artwork/georges-rouault-parade",
                             "internalID": "5ec5a29d4a8c34000ef03196",
                             "image": {
                                "aspect_ratio": 0.65,
                                "placeholder": "152.8013582342954%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/00XmFFxH7qCkrTE1W0Ckzg/large.jpg"
                             },
                             "title": "Parade",
                             "image_title": "Georges Rouault, ‘Parade’, 1934",
                             "date": "1934",
                             "sale_message": "$150,000 - 200,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRlOTc2NDllNmJhNzEyMDAwMTAwMjM1OA==",
                                   "href": "/artist/georges-rouault",
                                   "name": "Georges Rouault"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZWM1YTI5OTVkNGE5ODAwMTIxMDEyNjk=",
                             "slug": "georges-rouault-clown-et-enfant-2",
                             "href": "/artwork/georges-rouault-clown-et-enfant-2",
                             "internalID": "5ec5a2995d4a980012101269",
                             "image": {
                                "aspect_ratio": 0.69,
                                "placeholder": "144.23076923076923%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/1IW0xmaa2AUlNe8jyxOFww/large.jpg"
                             },
                             "title": "Clown et Enfant",
                             "image_title": "Georges Rouault, ‘Clown et Enfant’, 1930",
                             "date": "1930",
                             "sale_message": "$7,500 - 10,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRlOTc2NDllNmJhNzEyMDAwMTAwMjM1OA==",
                                   "href": "/artist/georges-rouault",
                                   "name": "Georges Rouault"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZTFjYmQxMjE0N2U4MzAwMTIwOTViNmE=",
                             "slug": "henri-de-toulouse-lautrec-divan-japonais-27",
                             "href": "/artwork/henri-de-toulouse-lautrec-divan-japonais-27",
                             "internalID": "5e1cbd12147e830012095b6a",
                             "image": {
                                "aspect_ratio": 0.75,
                                "placeholder": "132.95687885010267%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/rOgztp20GC_ul-Am9RgUgg/large.jpg"
                             },
                             "title": "Divan Japonais",
                             "image_title": "Henri de Toulouse-Lautrec, ‘Divan Japonais’, 1895",
                             "date": "1895",
                             "sale_message": "$7,500 - 10,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRlZGY5Yjg4OTAxOTJiMDAwMTAwMTc4OQ==",
                                   "href": "/artist/henri-de-toulouse-lautrec",
                                   "name": "Henri de Toulouse-Lautrec"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ODgzZDRiYzEzOWIyMTAzMWUwMDM1Y2U=",
                             "slug": "henri-de-toulouse-lautrec-jane-avril-jardin-de-paris",
                             "href": "/artwork/henri-de-toulouse-lautrec-jane-avril-jardin-de-paris",
                             "internalID": "5883d4bc139b21031e0035ce",
                             "image": {
                                "aspect_ratio": 0.75,
                                "placeholder": "133.48017621145374%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/yVf2v4G-QgEbnDDbdTMF3w/large.jpg"
                             },
                             "title": "Jane Avril - Jardin De Paris",
                             "image_title": "Henri de Toulouse-Lautrec, ‘Jane Avril - Jardin De Paris’, 1898",
                             "date": "1898",
                             "sale_message": "$7,500 - 10,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRlZGY5Yjg4OTAxOTJiMDAwMTAwMTc4OQ==",
                                   "href": "/artist/henri-de-toulouse-lautrec",
                                   "name": "Henri de Toulouse-Lautrec"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZTFmZGE1NDQzMTBjODAwMGZkZDI4OTY=",
                             "slug": "mary-cassatt-the-crocheting-lesson-4",
                             "href": "/artwork/mary-cassatt-the-crocheting-lesson-4",
                             "internalID": "5e1fda544310c8000fdd2896",
                             "image": {
                                "aspect_ratio": 0.61,
                                "placeholder": "164.23357664233578%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/PXp_1k6FhInyZzv99M6XzQ/large.jpg"
                             },
                             "title": "The Crocheting Lesson",
                             "image_title": "Mary Cassatt, ‘The Crocheting Lesson’, 1902",
                             "date": "1902",
                             "sale_message": "$40,000 - 50,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MmI3NGViNjhhMWIyYzAwMDQxZQ==",
                                   "href": "/artist/mary-cassatt",
                                   "name": "Mary Cassatt"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1Y2FiYTAzNTMyYzI5NTMyM2JkNjU2MzM=",
                             "slug": "alphonse-mucha-salon-des-cents",
                             "href": "/artwork/alphonse-mucha-salon-des-cents",
                             "internalID": "5caba03532c295323bd65633",
                             "image": {
                                "aspect_ratio": 0.67,
                                "placeholder": "148.5148514851485%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/zVERnQ3TkrYJcokNH6K3yA/large.jpg"
                             },
                             "title": "Salon Des Cents",
                             "image_title": "Alphonse Mucha, ‘Salon Des Cents’, 1897",
                             "date": "1897",
                             "sale_message": "$7,500 - 10,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                 "__typename": "ArtistArtworkGrid",
                 "title": "Other works by Alphonse Mucha",
                 "ctaTitle": "View all works by Alphonse Mucha",
                 "ctaHref": "/artist/alphonse-mucha",
                 "artworksConnection": {
                    "edges": [
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1M2NlYmU1MDcyNjE2OTQyNDcxMDAxMDA=",
                             "slug": "alphonse-mucha-lorenzaccio",
                             "href": "/artwork/alphonse-mucha-lorenzaccio",
                             "internalID": "53cebe507261694247100100",
                             "image": {
                                "aspect_ratio": 0.38,
                                "placeholder": "263.15789473684214%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/H-x6cmA8HIiTQO9JTR51NA/large.jpg"
                             },
                             "title": "LORENZACCIO",
                             "image_title": "Alphonse Mucha, ‘LORENZACCIO’, 1898",
                             "date": "1898",
                             "sale_message": "Contact For Price",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Christopher-Clark Fine Art",
                                "href": "/christopher-clark-fine-art",
                                "id": "UGFydG5lcjo1MmIyMGY1NDEzOWIyMTQyYzQwMDAwNGQ=",
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
                             "id": "QXJ0d29yazo1MjVkN2FlZTc2MjJkZGU1NGUwMDAxYjY=",
                             "slug": "alphonse-mucha-la-samaritaine",
                             "href": "/artwork/alphonse-mucha-la-samaritaine",
                             "internalID": "525d7aee7622dde54e0001b6",
                             "image": {
                                "aspect_ratio": 0.65,
                                "placeholder": "152.83842794759826%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/Me8KG4eU7acHbNdxVQRYJA/large.jpg"
                             },
                             "title": "La Samaritaine",
                             "image_title": "Alphonse Mucha, ‘La Samaritaine’, 1899",
                             "date": "1899",
                             "sale_message": "Contact For Price",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Contessa Gallery",
                                "href": "/contessa-gallery",
                                "id": "UGFydG5lcjo1MjRiNDRhNjljMThkYjllZmEwMDAwZjI=",
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
                             "id": "QXJ0d29yazo1ZDk2MzBiYjVmZjMzOTAwMTM3NjU2MGI=",
                             "slug": "alphonse-mucha-job-21",
                             "href": "/artwork/alphonse-mucha-job-21",
                             "internalID": "5d9630bb5ff339001376560b",
                             "image": {
                                "aspect_ratio": 0.65,
                                "placeholder": "153.57142857142858%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/eLndsQDFY_lb6FkaAkt7nA/large.jpg"
                             },
                             "title": "Job",
                             "image_title": "Alphonse Mucha, ‘Job’, 1898",
                             "date": "1898",
                             "sale_message": None,
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Isselbacher Gallery",
                                "href": "/isselbacher-gallery",
                                "id": "UGFydG5lcjo1OTc5MDFmY2FiNjBjYTYwZDI0NmNmZTE=",
                                "type": "Gallery"
                             },
                             "sale": None,
                             "sale_artwork": None,
                             "is_inquireable": False,
                             "is_saved": False,
                             "is_biddable": False
                          }
                       },
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1YmEwMGZjMTYwY2FkOTVhMGJkYTIyM2Q=",
                             "slug": "alphonse-mucha-lorenzaccio-3",
                             "href": "/artwork/alphonse-mucha-lorenzaccio-3",
                             "internalID": "5ba00fc160cad95a0bda223d",
                             "image": {
                                "aspect_ratio": 0.57,
                                "placeholder": "175.31468531468533%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/yOEzUSGFBbGBtqhTLa157w/large.jpg"
                             },
                             "title": "Lorenzaccio",
                             "image_title": "Alphonse Mucha, ‘Lorenzaccio’",
                             "date": "",
                             "sale_message": None,
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Hindman",
                                "href": "/auction/leslie-hindman-auctioneers",
                                "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                "type": "Auction House"
                             },
                             "sale": {
                                "is_auction": True,
                                "is_closed": True,
                                "id": "U2FsZTo1YjlhYjhmNTI4MzViNDYzM2IyZmQ0ZDg=",
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
                                   "display": "$250"
                                },
                                "id": "U2FsZUFydHdvcms6NWJhMDBmYzI3YWY4NmIwNjQyOTYzZTU2"
                             },
                             "is_inquireable": False,
                             "is_saved": False,
                             "is_biddable": False
                          }
                       },
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1YmEwMGZlNWRhMDFiNDFjYmUzNzA5YmY=",
                             "slug": "alphonse-mucha-chansons-daieules",
                             "href": "/artwork/alphonse-mucha-chansons-daieules",
                             "internalID": "5ba00fe5da01b41cbe3709bf",
                             "image": {
                                "aspect_ratio": 0.73,
                                "placeholder": "136.92762186115215%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/LhLdQXWyB-08UJdfO4BHXw/large.jpg"
                             },
                             "title": "Chansons d'Aieules",
                             "image_title": "Alphonse Mucha, ‘Chansons d'Aieules’",
                             "date": "",
                             "sale_message": None,
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Hindman",
                                "href": "/auction/leslie-hindman-auctioneers",
                                "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                "type": "Auction House"
                             },
                             "sale": {
                                "is_auction": True,
                                "is_closed": True,
                                "id": "U2FsZTo1YjlhYjhmNTI4MzViNDYzM2IyZmQ0ZDg=",
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
                                   "display": "$400"
                                },
                                "id": "U2FsZUFydHdvcms6NWJhMDBmZTYxNjc5NWMyZWY0MDA3ZjA4"
                             },
                             "is_inquireable": False,
                             "is_saved": False,
                             "is_biddable": False
                          }
                       },
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1YmExMmUwYjA5NjQxNzFjNjhhMTFiMTM=",
                             "slug": "alphonse-mucha-lautomne",
                             "href": "/artwork/alphonse-mucha-lautomne",
                             "internalID": "5ba12e0b0964171c68a11b13",
                             "image": {
                                "aspect_ratio": 0.43,
                                "placeholder": "231.8579766536965%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/d5a2sVRnEaxj8u1nfcLMYg/large.jpg"
                             },
                             "title": "L'Automne",
                             "image_title": "Alphonse Mucha, ‘L'Automne’, c. 1903",
                             "date": "c. 1903",
                             "sale_message": None,
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Hindman",
                                "href": "/auction/leslie-hindman-auctioneers",
                                "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                "type": "Auction House"
                             },
                             "sale": {
                                "is_auction": True,
                                "is_closed": True,
                                "id": "U2FsZTo1YmEwMTg5OTJiMmZlZjAwMjkxZWNiMDk=",
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
                                   "display": "$120"
                                },
                                "opening_bid": {
                                   "display": "$100"
                                },
                                "id": "U2FsZUFydHdvcms6NWJhMTJlMGVhZGJlYzczZTQ3ZDIxYzBk"
                             },
                             "is_inquireable": False,
                             "is_saved": False,
                             "is_biddable": False
                          }
                       },
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1M2NlYmU1ZjcyNjE2OTQyNDcxYTAxMDA=",
                             "slug": "alphonse-mucha-la-dame-aux-camelias",
                             "href": "/artwork/alphonse-mucha-la-dame-aux-camelias",
                             "internalID": "53cebe5f72616942471a0100",
                             "image": {
                                "aspect_ratio": 0.38,
                                "placeholder": "263.15789473684214%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/DmXSXMSGpo5fGT0WKc3uYg/large.jpg"
                             },
                             "title": "La Dame Aux Camélias",
                             "image_title": "Alphonse Mucha, ‘La Dame Aux Camélias’, 1898",
                             "date": "1898",
                             "sale_message": "Contact For Price",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Christopher-Clark Fine Art",
                                "href": "/christopher-clark-fine-art",
                                "id": "UGFydG5lcjo1MmIyMGY1NDEzOWIyMTQyYzQwMDAwNGQ=",
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
                             "id": "QXJ0d29yazo1Y2QxZTBmNzc4N2Q0ZTAwMTI1NGZkOTI=",
                             "slug": "alphonse-mucha-the-seasons-a-suite-of-four-works",
                             "href": "/artwork/alphonse-mucha-the-seasons-a-suite-of-four-works",
                             "internalID": "5cd1e0f7787d4e001254fd92",
                             "image": {
                                "aspect_ratio": 0.52,
                                "placeholder": "193.71794871794873%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/MzMOn0ZxhKjaVkq54qQ8Hg/large.jpg"
                             },
                             "title": "The Seasons  (a suite of four works)",
                             "image_title": "Alphonse Mucha, ‘The Seasons  (a suite of four works)’, 1896",
                             "date": "1896",
                             "sale_message": None,
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                   "href": "/artist/alphonse-mucha",
                                   "name": "Alphonse Mucha"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Hindman",
                                "href": "/auction/leslie-hindman-auctioneers",
                                "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                "type": "Auction House"
                             },
                             "sale": {
                                "is_auction": True,
                                "is_closed": True,
                                "id": "U2FsZTo1Y2QwNGY0ZDg3MzU4NTFkMDliM2QxNTg=",
                                "is_live_open": False,
                                "is_open": False,
                                "is_preview": False,
                                "display_timely_at": None
                             },
                             "sale_artwork": {
                                "counts": {
                                   "bidder_positions": 1
                                },
                                "highest_bid": {
                                   "display": "$6,000"
                                },
                                "opening_bid": {
                                   "display": "$6,000"
                                },
                                "id": "U2FsZUFydHdvcms6NWNkMWUwZjgyODdmMWE0ZjdjNWNlMzA2"
                             },
                             "is_inquireable": False,
                             "is_saved": False,
                             "is_biddable": False
                          }
                       }
                    ]
                 }
              },
              {
                 "__typename": "PartnerArtworkGrid",
                 "title": "Other works from Galerie d'Orsay",
                 "ctaTitle": "View all works from Galerie d'Orsay",
                 "ctaHref": "/galerie-dorsay",
                 "artworksConnection": {
                    "edges": [
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1ZmQzYWY1M2RlNTg1OTAwMTI3ZTMyY2Y=",
                             "slug": "ken-salaz-sunrise-over-walden-pond",
                             "href": "/artwork/ken-salaz-sunrise-over-walden-pond",
                             "internalID": "5fd3af53de585900127e32cf",
                             "image": {
                                "aspect_ratio": 1.63,
                                "placeholder": "61.4%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/suUXEypO9xJsYPj51uPMHQ/large.jpg"
                             },
                             "title": "Sunrise over Walden Pond",
                             "image_title": "Ken Salaz, ‘Sunrise over Walden Pond’, 2020",
                             "date": "2020",
                             "sale_message": "$2,500 - 5,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjU1NTRkYTQ5NzI2MTY5MGRhYTdkMDAwMA==",
                                   "href": "/artist/ken-salaz",
                                   "name": "Ken Salaz"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZmQzYWY1MjUzMGRmMDAwMTFjZDY5NGI=",
                             "slug": "ken-salaz-sunflare-off-walden-pond",
                             "href": "/artwork/ken-salaz-sunflare-off-walden-pond",
                             "internalID": "5fd3af52530df00011cd694b",
                             "image": {
                                "aspect_ratio": 1.36,
                                "placeholder": "73.32878581173262%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/hb8G9_s9wD1tgtXojA3Whw/large.jpg"
                             },
                             "title": "Sunflare off Walden Pond",
                             "image_title": "Ken Salaz, ‘Sunflare off Walden Pond’, 2020",
                             "date": "2020",
                             "sale_message": "$2,500 - 5,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjU1NTRkYTQ5NzI2MTY5MGRhYTdkMDAwMA==",
                                   "href": "/artist/ken-salaz",
                                   "name": "Ken Salaz"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZmQzYWY1MzAxY2I4YzAwMTI1NjM2YjQ=",
                             "slug": "ken-salaz-afternoon-sunlight-stroll-walden",
                             "href": "/artwork/ken-salaz-afternoon-sunlight-stroll-walden",
                             "internalID": "5fd3af5301cb8c00125636b4",
                             "image": {
                                "aspect_ratio": 1.32,
                                "placeholder": "75.66433566433567%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/NGC_LAwvOKejDKL43bTeKQ/large.jpg"
                             },
                             "title": "Afternoon Sunlight Stroll - Walden",
                             "image_title": "Ken Salaz, ‘Afternoon Sunlight Stroll - Walden’, 2020",
                             "date": "2020",
                             "sale_message": "$2,500 - 5,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjU1NTRkYTQ5NzI2MTY5MGRhYTdkMDAwMA==",
                                   "href": "/artist/ken-salaz",
                                   "name": "Ken Salaz"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZmQzYWY1MjEyZDE1OTQxMDA4OTc2NWU=",
                             "slug": "ken-salaz-journey-home",
                             "href": "/artwork/ken-salaz-journey-home",
                             "internalID": "5fd3af5212d159410089765e",
                             "image": {
                                "aspect_ratio": 2.02,
                                "placeholder": "49.6%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/kZJhOerwVdMKXVldaT4mGg/large.jpg"
                             },
                             "title": "Journey Home",
                             "image_title": "Ken Salaz, ‘Journey Home’, 2013",
                             "date": "2013",
                             "sale_message": "$7,500 - 10,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjU1NTRkYTQ5NzI2MTY5MGRhYTdkMDAwMA==",
                                   "href": "/artist/ken-salaz",
                                   "name": "Ken Salaz"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZmQzYWY3MzkxYWRiZjAwMTJlMGJiY2U=",
                             "slug": "damien-hirst-histidyl-7",
                             "href": "/artwork/damien-hirst-histidyl-7",
                             "internalID": "5fd3af7391adbf0012e0bbce",
                             "image": {
                                "aspect_ratio": 1.26,
                                "placeholder": "79.22222222222223%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/6mIxd08Z9PFZ2LHNKsytFQ/large.jpg"
                             },
                             "title": "Histidyl",
                             "image_title": "Damien Hirst, ‘Histidyl’, 2008",
                             "date": "2008",
                             "sale_message": "$15,000 - 20,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjZhNGViNjhhMWIyYzAwMDBhZQ==",
                                   "href": "/artist/damien-hirst",
                                   "name": "Damien Hirst"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZmJhYTk4YjU0MDg1ZTAwMGU3YmNkOWQ=",
                             "slug": "salvador-dali-turtle-mountain-1",
                             "href": "/artwork/salvador-dali-turtle-mountain-1",
                             "internalID": "5fbaa98b54085e000e7bcd9d",
                             "image": {
                                "aspect_ratio": 0.76,
                                "placeholder": "131.67587476979742%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/N6skYA7GBaTf_q87ui104w/large.jpg"
                             },
                             "title": "Turtle Mountain",
                             "image_title": "Salvador Dalí, ‘Turtle Mountain’, 1967",
                             "date": "1967",
                             "sale_message": "$2,500 - 5,000",
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
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZmJhYTk4YjQyNjBlZDNjY2NkOWYzOTI=",
                             "slug": "salvador-dali-magic-circle",
                             "href": "/artwork/salvador-dali-magic-circle",
                             "internalID": "5fbaa98b4260ed3cccd9f392",
                             "image": {
                                "aspect_ratio": 0.58,
                                "placeholder": "171.875%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/vuop_F876C8GrpDcpWH5QQ/large.jpg"
                             },
                             "title": "Magic Circle",
                             "image_title": "Salvador Dalí, ‘Magic Circle’, 1968",
                             "date": "1968",
                             "sale_message": "$5,000 - 7,500",
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
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1ZmJhYTk4YjRkZWNhZDAwMTJiYzZiN2Y=",
                             "slug": "salvador-dali-petite-horses-1",
                             "href": "/artwork/salvador-dali-petite-horses-1",
                             "internalID": "5fbaa98b4decad0012bc6b7f",
                             "image": {
                                "aspect_ratio": 0.73,
                                "placeholder": "136.6742596810934%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/Z1iNXjNULNlfF9KDRL0ktg/large.jpg"
                             },
                             "title": "Petite Horses",
                             "image_title": "Salvador Dalí, ‘Petite Horses’, 1967",
                             "date": "1967",
                             "sale_message": "$7,500 - 10,000",
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
                                "name": "Galerie d'Orsay",
                                "href": "/galerie-dorsay",
                                "id": "UGFydG5lcjo1NTdmMWE5Mjc3NmY3MjYwYjIwMDAwZmQ=",
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
                             "id": "QXJ0d29yazo1MjVkN2RiMjljMThkYjY2YzUwMDA2YWU=",
                             "slug": "pierre-auguste-renoir-claude-renoir-tourne-a-gauche",
                             "href": "/artwork/pierre-auguste-renoir-claude-renoir-tourne-a-gauche",
                             "internalID": "525d7db29c18db66c50006ae",
                             "image": {
                                "aspect_ratio": 0.84,
                                "placeholder": "119.65811965811966%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/_TNO-d0fxLDqPZbSNU6VIg/large.jpg"
                             },
                             "title": "Claude Renoir, Tourne a Gauche",
                             "image_title": "Pierre-Auguste Renoir, ‘Claude Renoir, Tourne a Gauche’, ca. 1904",
                             "date": "ca. 1904",
                             "sale_message": "Contact For Price",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjljNGViNjhhMWIyYzAwMDJlMA==",
                                   "href": "/artist/pierre-auguste-renoir",
                                   "name": "Pierre-Auguste Renoir"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Contessa Gallery",
                                "href": "/contessa-gallery",
                                "id": "UGFydG5lcjo1MjRiNDRhNjljMThkYjllZmEwMDAwZjI=",
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
                             "id": "QXJ0d29yazo1OGY3ZWYzNzI3NWIyNDAzY2Q1MDU0Zjc=",
                             "slug": "henri-matisse-visage-legerement-penche-vers-la-gauche-8",
                             "href": "/artwork/henri-matisse-visage-legerement-penche-vers-la-gauche-8",
                             "internalID": "58f7ef37275b2403cd5054f7",
                             "image": {
                                "aspect_ratio": 0.66,
                                "placeholder": "152.0190023752969%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/RRa4bmBuDuW-srVcciKAkg/large.jpg"
                             },
                             "title": "Visage Légèrement Penché vers la Gauche",
                             "image_title": "Henri Matisse, ‘Visage Légèrement Penché vers la Gauche’, 1913",
                             "date": "1913",
                             "sale_message": "Contact For Price",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjkzNGViNjhhMWIyYzAwMDI1YQ==",
                                   "href": "/artist/henri-matisse",
                                   "name": "Henri Matisse"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie Maximillian",
                                "href": "/galerie-maximillian",
                                "id": "UGFydG5lcjo1MmZhNDZjNWM5ZGMyNDcxNzcwMDAxNzM=",
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
                             "id": "QXJ0d29yazo1YTc4YjE4MTJhODkzYTYwNzllN2M4YjU=",
                             "slug": "alfred-kubin-der-beste-arzt",
                             "href": "/artwork/alfred-kubin-der-beste-arzt",
                             "internalID": "5a78b1812a893a6079e7c8b5",
                             "image": {
                                "aspect_ratio": 1.33,
                                "placeholder": "75%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/uXKNQamSIurz5QuKOVR2HQ/large.jpg"
                             },
                             "title": "Der Beste Arzt",
                             "image_title": "Alfred Kubin, ‘Der Beste Arzt’, 1900-1909",
                             "date": "1900-1909",
                             "sale_message": "Sold",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjUwNmIzYTBjN2VkYzg5MDAwMjAwMGRhZA==",
                                   "href": "/artist/alfred-kubin",
                                   "name": "Alfred Kubin"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Lions Gallery",
                                "href": "/lions-gallery",
                                "id": "UGFydG5lcjo1YTQxNTllMGIyMDJhMzUwNDEyZThlN2I=",
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
                             "id": "QXJ0d29yazo1ZDVjZmZjYjAyZTcyZjAwMTE2YWM3NTM=",
                             "slug": "egon-schiele-portrait-of-a-woman-1",
                             "href": "/artwork/egon-schiele-portrait-of-a-woman-1",
                             "internalID": "5d5cffcb02e72f00116ac753",
                             "image": {
                                "aspect_ratio": 0.64,
                                "placeholder": "155.57437200112898%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/dEfGhyjSZS2ex-lXuC6HrA/large.jpg"
                             },
                             "title": "Portrait of a Woman",
                             "image_title": "Egon Schiele, ‘Portrait of a Woman’, 1910",
                             "date": "1910",
                             "sale_message": "Sold",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRkOGI5MjgzNGViNjhhMWIyYzAwMDFhMA==",
                                   "href": "/artist/egon-schiele",
                                   "name": "Egon Schiele"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Galerie Kovacek & Zetter",
                                "href": "/galerie-kovacek-and-zetter",
                                "id": "UGFydG5lcjo1YTU2NDdkNWIyMDJhMzUxNzFjZmQ3NGE=",
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
                             "id": "QXJ0d29yazo1MTVkNmY2ZDVlZWIxYzUyNGMwMDRiNjg=",
                             "slug": "henri-de-toulouse-lautrec-mme-le-marguoin-milliner-mme-le-marguoin-modiste",
                             "href": "/artwork/henri-de-toulouse-lautrec-mme-le-marguoin-milliner-mme-le-marguoin-modiste",
                             "internalID": "515d6f6d5eeb1c524c004b68",
                             "image": {
                                "aspect_ratio": 0.76,
                                "placeholder": "132.15859030837004%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/n9NZ4P-0ZnbrACymAK2Vqg/large.jpg"
                             },
                             "title": "Mme. Le Marguoin, Milliner  (Mme. Le Marguoin, modiste)",
                             "image_title": "Henri de Toulouse-Lautrec, ‘Mme. Le Marguoin, Milliner  (Mme. Le Marguoin, modiste)’, 1900",
                             "date": "1900",
                             "sale_message": "Permanent collection",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRlZGY5Yjg4OTAxOTJiMDAwMTAwMTc4OQ==",
                                   "href": "/artist/henri-de-toulouse-lautrec",
                                   "name": "Henri de Toulouse-Lautrec"
                                }
                             ],
                             "collecting_institution": "National Gallery of Art, Washington D.C.",
                             "partner": {
                                "name": "National Gallery of Art, Washington, D.C.",
                                "href": "/ngadc",
                                "id": "UGFydG5lcjo0Zjk5YzdiNzkzYWI0YjAwMDEwMDAxNzk=",
                                "type": "Institution"
                             },
                             "sale": None,
                             "sale_artwork": None,
                             "is_inquireable": False,
                             "is_saved": False,
                             "is_biddable": False
                          }
                       },
                       {
                          "__typename": "ArtworkEdge",
                          "node": {
                             "id": "QXJ0d29yazo1ZTg0Yjc4M2M1NGQxYzAwMTJmZDU4ODg=",
                             "slug": "odilon-redon-planche-dessai-no-1-femme-au-hennin",
                             "href": "/artwork/odilon-redon-planche-dessai-no-1-femme-au-hennin",
                             "internalID": "5e84b783c54d1c0012fd5888",
                             "image": {
                                "aspect_ratio": 0.79,
                                "placeholder": "126.87000726216414%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/X3HxYWT-Uykus_ioeaCOBw/large.jpg"
                             },
                             "title": "Planche d'Essai No. 1: Femme au Hennin",
                             "image_title": "Odilon Redon, ‘Planche d'Essai No. 1: Femme au Hennin’, 1900",
                             "date": "1900",
                             "sale_message": "$3,000",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjRlZTY4YzdlNmIxN2NmMDAwMTAwMjRkMA==",
                                   "href": "/artist/odilon-redon",
                                   "name": "Odilon Redon"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Childs Gallery",
                                "href": "/childs-gallery",
                                "id": "UGFydG5lcjo1MjI2Njk1NmViYWQ2NGQ0YTYwMDAwNWI=",
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
                             "id": "QXJ0d29yazo1Yjg2ZTZiYjczZDY3NDAwMmEyZjY0NjA=",
                             "slug": "jules-cheret-grand-theatre-of-the-fair-plate-221",
                             "href": "/artwork/jules-cheret-grand-theatre-of-the-fair-plate-221",
                             "internalID": "5b86e6bb73d674002a2f6460",
                             "image": {
                                "aspect_ratio": 0.69,
                                "placeholder": "144.92753623188406%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/L7BmWiQbPyNgBUPcwxk24Q/large.jpg"
                             },
                             "title": "Grand Theatre of the Fair (Plate 221)",
                             "image_title": "Jules Chéret, ‘Grand Theatre of the Fair (Plate 221)’, 1900",
                             "date": "1900",
                             "sale_message": "$995",
                             "cultural_maker": None,
                             "artists": [
                                {
                                   "id": "QXJ0aXN0OjUxNWIwN2E3MjIzYWZhN2VhODAwMDE4MQ==",
                                   "href": "/artist/jules-cheret",
                                   "name": "Jules Chéret"
                                }
                             ],
                             "collecting_institution": None,
                             "partner": {
                                "name": "Martin Lawrence Galleries",
                                "href": "/martin-lawrence-galleries",
                                "id": "UGFydG5lcjo1YWEyZTkxZjhiM2I4MTdiMTZhNmQ4NjE=",
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
                             "id": "QXJ0d29yazo1Y2U0MmE5Yjg2ZTRlOTFjNDA3NzA4NzQ=",
                             "slug": "pablo-picasso-arlequin-moustachu-a-la-guitare-1",
                             "href": "/artwork/pablo-picasso-arlequin-moustachu-a-la-guitare-1",
                             "internalID": "5ce42a9b86e4e91c40770874",
                             "image": {
                                "aspect_ratio": 0.79,
                                "placeholder": "126%",
                                "url": "https://d32dm0rphc51dk.cloudfront.net/3PMtIHQSt9_5K8X5yzs8BA/large.jpg"
                             },
                             "title": "Arlequin Moustachu a la Guitare",
                             "image_title": "Pablo Picasso, ‘Arlequin Moustachu a la Guitare’, 1973 original created in 1916",
                             "date": "1973 original created in 1916",
                             "sale_message": "$3,600",
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
                                "name": "RoGallery",
                                "href": "/rogallery",
                                "id": "UGFydG5lcjo1NzBiZjRhNmNkNTMwZTY1OTEwMDBhYzQ=",
                                "type": "Gallery"
                             },
                             "sale": None,
                             "sale_artwork": None,
                             "is_inquireable": False,
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
                          "id": "QXJ0d29yazo1MjVkN2RiMjljMThkYjY2YzUwMDA2YWU=",
                          "slug": "pierre-auguste-renoir-claude-renoir-tourne-a-gauche",
                          "href": "/artwork/pierre-auguste-renoir-claude-renoir-tourne-a-gauche",
                          "internalID": "525d7db29c18db66c50006ae",
                          "image": {
                             "aspect_ratio": 0.84,
                             "placeholder": "119.65811965811966%",
                             "url": "https://d32dm0rphc51dk.cloudfront.net/_TNO-d0fxLDqPZbSNU6VIg/large.jpg"
                          },
                          "title": "Claude Renoir, Tourne a Gauche",
                          "image_title": "Pierre-Auguste Renoir, ‘Claude Renoir, Tourne a Gauche’, ca. 1904",
                          "date": "ca. 1904",
                          "sale_message": "Contact For Price",
                          "cultural_maker": None,
                          "artists": [
                             {
                                "id": "QXJ0aXN0OjRkOGI5MjljNGViNjhhMWIyYzAwMDJlMA==",
                                "href": "/artist/pierre-auguste-renoir",
                                "name": "Pierre-Auguste Renoir"
                             }
                          ],
                          "collecting_institution": None,
                          "partner": {
                             "name": "Contessa Gallery",
                             "href": "/contessa-gallery",
                             "id": "UGFydG5lcjo1MjRiNDRhNjljMThkYjllZmEwMDAwZjI=",
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
                          "id": "QXJ0d29yazo1OGY3ZWYzNzI3NWIyNDAzY2Q1MDU0Zjc=",
                          "slug": "henri-matisse-visage-legerement-penche-vers-la-gauche-8",
                          "href": "/artwork/henri-matisse-visage-legerement-penche-vers-la-gauche-8",
                          "internalID": "58f7ef37275b2403cd5054f7",
                          "image": {
                             "aspect_ratio": 0.66,
                             "placeholder": "152.0190023752969%",
                             "url": "https://d32dm0rphc51dk.cloudfront.net/RRa4bmBuDuW-srVcciKAkg/large.jpg"
                          },
                          "title": "Visage Légèrement Penché vers la Gauche",
                          "image_title": "Henri Matisse, ‘Visage Légèrement Penché vers la Gauche’, 1913",
                          "date": "1913",
                          "sale_message": "Contact For Price",
                          "cultural_maker": None,
                          "artists": [
                             {
                                "id": "QXJ0aXN0OjRkOGI5MjkzNGViNjhhMWIyYzAwMDI1YQ==",
                                "href": "/artist/henri-matisse",
                                "name": "Henri Matisse"
                             }
                          ],
                          "collecting_institution": None,
                          "partner": {
                             "name": "Galerie Maximillian",
                             "href": "/galerie-maximillian",
                             "id": "UGFydG5lcjo1MmZhNDZjNWM5ZGMyNDcxNzcwMDAxNzM=",
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
                          "id": "QXJ0d29yazo1YTc4YjE4MTJhODkzYTYwNzllN2M4YjU=",
                          "slug": "alfred-kubin-der-beste-arzt",
                          "href": "/artwork/alfred-kubin-der-beste-arzt",
                          "internalID": "5a78b1812a893a6079e7c8b5",
                          "image": {
                             "aspect_ratio": 1.33,
                             "placeholder": "75%",
                             "url": "https://d32dm0rphc51dk.cloudfront.net/uXKNQamSIurz5QuKOVR2HQ/large.jpg"
                          },
                          "title": "Der Beste Arzt",
                          "image_title": "Alfred Kubin, ‘Der Beste Arzt’, 1900-1909",
                          "date": "1900-1909",
                          "sale_message": "Sold",
                          "cultural_maker": None,
                          "artists": [
                             {
                                "id": "QXJ0aXN0OjUwNmIzYTBjN2VkYzg5MDAwMjAwMGRhZA==",
                                "href": "/artist/alfred-kubin",
                                "name": "Alfred Kubin"
                             }
                          ],
                          "collecting_institution": None,
                          "partner": {
                             "name": "Lions Gallery",
                             "href": "/lions-gallery",
                             "id": "UGFydG5lcjo1YTQxNTllMGIyMDJhMzUwNDEyZThlN2I=",
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
                          "id": "QXJ0d29yazo1ZDVjZmZjYjAyZTcyZjAwMTE2YWM3NTM=",
                          "slug": "egon-schiele-portrait-of-a-woman-1",
                          "href": "/artwork/egon-schiele-portrait-of-a-woman-1",
                          "internalID": "5d5cffcb02e72f00116ac753",
                          "image": {
                             "aspect_ratio": 0.64,
                             "placeholder": "155.57437200112898%",
                             "url": "https://d32dm0rphc51dk.cloudfront.net/dEfGhyjSZS2ex-lXuC6HrA/large.jpg"
                          },
                          "title": "Portrait of a Woman",
                          "image_title": "Egon Schiele, ‘Portrait of a Woman’, 1910",
                          "date": "1910",
                          "sale_message": "Sold",
                          "cultural_maker": None,
                          "artists": [
                             {
                                "id": "QXJ0aXN0OjRkOGI5MjgzNGViNjhhMWIyYzAwMDFhMA==",
                                "href": "/artist/egon-schiele",
                                "name": "Egon Schiele"
                             }
                          ],
                          "collecting_institution": None,
                          "partner": {
                             "name": "Galerie Kovacek & Zetter",
                             "href": "/galerie-kovacek-and-zetter",
                             "id": "UGFydG5lcjo1YTU2NDdkNWIyMDJhMzUxNzFjZmQ3NGE=",
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
                          "id": "QXJ0d29yazo1MTVkNmY2ZDVlZWIxYzUyNGMwMDRiNjg=",
                          "slug": "henri-de-toulouse-lautrec-mme-le-marguoin-milliner-mme-le-marguoin-modiste",
                          "href": "/artwork/henri-de-toulouse-lautrec-mme-le-marguoin-milliner-mme-le-marguoin-modiste",
                          "internalID": "515d6f6d5eeb1c524c004b68",
                          "image": {
                             "aspect_ratio": 0.76,
                             "placeholder": "132.15859030837004%",
                             "url": "https://d32dm0rphc51dk.cloudfront.net/n9NZ4P-0ZnbrACymAK2Vqg/large.jpg"
                          },
                          "title": "Mme. Le Marguoin, Milliner  (Mme. Le Marguoin, modiste)",
                          "image_title": "Henri de Toulouse-Lautrec, ‘Mme. Le Marguoin, Milliner  (Mme. Le Marguoin, modiste)’, 1900",
                          "date": "1900",
                          "sale_message": "Permanent collection",
                          "cultural_maker": None,
                          "artists": [
                             {
                                "id": "QXJ0aXN0OjRlZGY5Yjg4OTAxOTJiMDAwMTAwMTc4OQ==",
                                "href": "/artist/henri-de-toulouse-lautrec",
                                "name": "Henri de Toulouse-Lautrec"
                             }
                          ],
                          "collecting_institution": "National Gallery of Art, Washington D.C.",
                          "partner": {
                             "name": "National Gallery of Art, Washington, D.C.",
                             "href": "/ngadc",
                             "id": "UGFydG5lcjo0Zjk5YzdiNzkzYWI0YjAwMDEwMDAxNzk=",
                             "type": "Institution"
                          },
                          "sale": None,
                          "sale_artwork": None,
                          "is_inquireable": False,
                          "is_saved": False,
                          "is_biddable": False
                       }
                    },
                    {
                       "__typename": "ArtworkEdge",
                       "node": {
                          "id": "QXJ0d29yazo1ZTg0Yjc4M2M1NGQxYzAwMTJmZDU4ODg=",
                          "slug": "odilon-redon-planche-dessai-no-1-femme-au-hennin",
                          "href": "/artwork/odilon-redon-planche-dessai-no-1-femme-au-hennin",
                          "internalID": "5e84b783c54d1c0012fd5888",
                          "image": {
                             "aspect_ratio": 0.79,
                             "placeholder": "126.87000726216414%",
                             "url": "https://d32dm0rphc51dk.cloudfront.net/X3HxYWT-Uykus_ioeaCOBw/large.jpg"
                          },
                          "title": "Planche d'Essai No. 1: Femme au Hennin",
                          "image_title": "Odilon Redon, ‘Planche d'Essai No. 1: Femme au Hennin’, 1900",
                          "date": "1900",
                          "sale_message": "$3,000",
                          "cultural_maker": None,
                          "artists": [
                             {
                                "id": "QXJ0aXN0OjRlZTY4YzdlNmIxN2NmMDAwMTAwMjRkMA==",
                                "href": "/artist/odilon-redon",
                                "name": "Odilon Redon"
                             }
                          ],
                          "collecting_institution": None,
                          "partner": {
                             "name": "Childs Gallery",
                             "href": "/childs-gallery",
                             "id": "UGFydG5lcjo1MjI2Njk1NmViYWQ2NGQ0YTYwMDAwNWI=",
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
                          "id": "QXJ0d29yazo1Yjg2ZTZiYjczZDY3NDAwMmEyZjY0NjA=",
                          "slug": "jules-cheret-grand-theatre-of-the-fair-plate-221",
                          "href": "/artwork/jules-cheret-grand-theatre-of-the-fair-plate-221",
                          "internalID": "5b86e6bb73d674002a2f6460",
                          "image": {
                             "aspect_ratio": 0.69,
                             "placeholder": "144.92753623188406%",
                             "url": "https://d32dm0rphc51dk.cloudfront.net/L7BmWiQbPyNgBUPcwxk24Q/large.jpg"
                          },
                          "title": "Grand Theatre of the Fair (Plate 221)",
                          "image_title": "Jules Chéret, ‘Grand Theatre of the Fair (Plate 221)’, 1900",
                          "date": "1900",
                          "sale_message": "$995",
                          "cultural_maker": None,
                          "artists": [
                             {
                                "id": "QXJ0aXN0OjUxNWIwN2E3MjIzYWZhN2VhODAwMDE4MQ==",
                                "href": "/artist/jules-cheret",
                                "name": "Jules Chéret"
                             }
                          ],
                          "collecting_institution": None,
                          "partner": {
                             "name": "Martin Lawrence Galleries",
                             "href": "/martin-lawrence-galleries",
                             "id": "UGFydG5lcjo1YWEyZTkxZjhiM2I4MTdiMTZhNmQ4NjE=",
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
                          "id": "QXJ0d29yazo1Y2U0MmE5Yjg2ZTRlOTFjNDA3NzA4NzQ=",
                          "slug": "pablo-picasso-arlequin-moustachu-a-la-guitare-1",
                          "href": "/artwork/pablo-picasso-arlequin-moustachu-a-la-guitare-1",
                          "internalID": "5ce42a9b86e4e91c40770874",
                          "image": {
                             "aspect_ratio": 0.79,
                             "placeholder": "126%",
                             "url": "https://d32dm0rphc51dk.cloudfront.net/3PMtIHQSt9_5K8X5yzs8BA/large.jpg"
                          },
                          "title": "Arlequin Moustachu a la Guitare",
                          "image_title": "Pablo Picasso, ‘Arlequin Moustachu a la Guitare’, 1973 original created in 1916",
                          "date": "1973 original created in 1916",
                          "sale_message": "$3,600",
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
                             "name": "RoGallery",
                             "href": "/rogallery",
                             "id": "UGFydG5lcjo1NzBiZjRhNmNkNTMwZTY1OTEwMDBhYzQ=",
                             "type": "Gallery"
                          },
                          "sale": None,
                          "sale_artwork": None,
                          "is_inquireable": False,
                          "is_saved": False,
                          "is_biddable": False
                       }
                    }
                 ]
              },
              "id": "QXJ0d29ya0xheWVyOm1haW4="
           },
           "artistSeriesConnection": {
              "edges": [
                 {
                    "node": {
                       "slug": "alphonse-mucha-job",
                       "internalID": "761c5d7a-85cc-44f0-9d27-213eab4fe3aa",
                       "filterArtworksConnection": {
                          "edges": [
                             {
                                "node": {
                                   "slug": "alphonse-mucha-job-31",
                                   "internalID": "5f5a351cb6ff97000fdeabe8",
                                   "image": {
                                      "url": "https://d32dm0rphc51dk.cloudfront.net/e6JEFiTAconIQV5607fbww/large.jpg",
                                      "aspectRatio": 0.73
                                   },
                                   "imageTitle": "Alphonse Mucha, ‘Job’, 1899",
                                   "title": "Job",
                                   "href": "/artwork/alphonse-mucha-job-31",
                                   "date": "1899",
                                   "sale_message": "Sold",
                                   "cultural_maker": None,
                                   "artists": [
                                      {
                                         "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                         "href": "/artist/alphonse-mucha",
                                         "name": "Alphonse Mucha"
                                      }
                                   ],
                                   "collecting_institution": None,
                                   "partner": {
                                      "name": "NCAG",
                                      "href": "/ncag",
                                      "id": "UGFydG5lcjo1YmZkN2ZjNTM4NTQwMjRmMjljMjJmNzM=",
                                      "type": "Gallery"
                                   },
                                   "sale": None,
                                   "sale_artwork": None,
                                   "is_inquireable": False,
                                   "id": "QXJ0d29yazo1ZjVhMzUxY2I2ZmY5NzAwMGZkZWFiZTg=",
                                   "is_saved": False,
                                   "is_biddable": False
                                }
                             },
                             {
                                "node": {
                                   "slug": "alphonse-mucha-job-32",
                                   "internalID": "5fad8605ef6b3200125d1c42",
                                   "image": {
                                      "url": "https://d32dm0rphc51dk.cloudfront.net/nyLdNZBbnQq5UL3usk5bjA/large.jpg",
                                      "aspectRatio": 0.76
                                   },
                                   "imageTitle": "Alphonse Mucha, ‘Job’, 1896",
                                   "title": "Job",
                                   "href": "/artwork/alphonse-mucha-job-32",
                                   "date": "1896",
                                   "sale_message": None,
                                   "cultural_maker": None,
                                   "artists": [
                                      {
                                         "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                         "href": "/artist/alphonse-mucha",
                                         "name": "Alphonse Mucha"
                                      }
                                   ],
                                   "collecting_institution": None,
                                   "partner": {
                                      "name": "Hindman",
                                      "href": "/auction/leslie-hindman-auctioneers",
                                      "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                      "type": "Auction House"
                                   },
                                   "sale": {
                                      "is_auction": True,
                                      "is_closed": True,
                                      "id": "U2FsZTo1ZmFkN2UyNGM1M2ExYjAwMTI4ZDA5ODY=",
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
                                         "display": "$5,000"
                                      },
                                      "id": "U2FsZUFydHdvcms6NWZhZDg2MDcyYjA4OTgwMDEyNWVjNjlm"
                                   },
                                   "is_inquireable": False,
                                   "id": "QXJ0d29yazo1ZmFkODYwNWVmNmIzMjAwMTI1ZDFjNDI=",
                                   "is_saved": False,
                                   "is_biddable": False
                                }
                             },
                             {
                                "node": {
                                   "slug": "alphonse-mucha-job-16",
                                   "internalID": "5c1bc8da1310911d6b00283e",
                                   "image": {
                                      "url": "https://d32dm0rphc51dk.cloudfront.net/SOg40ztkfIqgOTElXASkiA/large.jpg",
                                      "aspectRatio": 0.69
                                   },
                                   "imageTitle": "Alphonse Mucha, ‘Job’, 1896",
                                   "title": "Job",
                                   "href": "/artwork/alphonse-mucha-job-16",
                                   "date": "1896",
                                   "sale_message": None,
                                   "cultural_maker": None,
                                   "artists": [
                                      {
                                         "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                         "href": "/artist/alphonse-mucha",
                                         "name": "Alphonse Mucha"
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
                                      "id": "U2FsZTo1YzFhNzYwNDhiYTJiNjYxMDlhYWYzNTk=",
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
                                         "display": "£7,000"
                                      },
                                      "id": "U2FsZUFydHdvcms6NWMxYmM4ZGJjNTE2MzM1ZmFmMzhjNjM4"
                                   },
                                   "is_inquireable": False,
                                   "id": "QXJ0d29yazo1YzFiYzhkYTEzMTA5MTFkNmIwMDI4M2U=",
                                   "is_saved": False,
                                   "is_biddable": False
                                }
                             },
                             {
                                "node": {
                                   "slug": "alphonse-mucha-job-21",
                                   "internalID": "5d9630bb5ff339001376560b",
                                   "image": {
                                      "url": "https://d32dm0rphc51dk.cloudfront.net/eLndsQDFY_lb6FkaAkt7nA/large.jpg",
                                      "aspectRatio": 0.65
                                   },
                                   "imageTitle": "Alphonse Mucha, ‘Job’, 1898",
                                   "title": "Job",
                                   "href": "/artwork/alphonse-mucha-job-21",
                                   "date": "1898",
                                   "sale_message": None,
                                   "cultural_maker": None,
                                   "artists": [
                                      {
                                         "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                         "href": "/artist/alphonse-mucha",
                                         "name": "Alphonse Mucha"
                                      }
                                   ],
                                   "collecting_institution": None,
                                   "partner": {
                                      "name": "Isselbacher Gallery",
                                      "href": "/isselbacher-gallery",
                                      "id": "UGFydG5lcjo1OTc5MDFmY2FiNjBjYTYwZDI0NmNmZTE=",
                                      "type": "Gallery"
                                   },
                                   "sale": None,
                                   "sale_artwork": None,
                                   "is_inquireable": False,
                                   "id": "QXJ0d29yazo1ZDk2MzBiYjVmZjMzOTAwMTM3NjU2MGI=",
                                   "is_saved": False,
                                   "is_biddable": False
                                }
                             },
                             {
                                "node": {
                                   "slug": "alphonse-mucha-job-15",
                                   "internalID": "5bc131970ac6a60345d21230",
                                   "image": {
                                      "url": "https://d32dm0rphc51dk.cloudfront.net/lN_lSsTft4tw442DvmTTjg/large.jpg",
                                      "aspectRatio": 0.67
                                   },
                                   "imageTitle": "Alphonse Mucha, ‘Job’, 1898",
                                   "title": "Job",
                                   "href": "/artwork/alphonse-mucha-job-15",
                                   "date": "1898",
                                   "sale_message": None,
                                   "cultural_maker": None,
                                   "artists": [
                                      {
                                         "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                         "href": "/artist/alphonse-mucha",
                                         "name": "Alphonse Mucha"
                                      }
                                   ],
                                   "collecting_institution": None,
                                   "partner": {
                                      "name": "Christie's",
                                      "href": "/auction/partner-553e693d7261695a85350100",
                                      "id": "UGFydG5lcjo1NTNlNjkzZDcyNjE2OTVhODUzNTAxMDA=",
                                      "type": "Auction House"
                                   },
                                   "sale": {
                                      "is_auction": True,
                                      "is_closed": True,
                                      "id": "U2FsZTo1YmJhYWVmYTZlOTY0ZDE4MmY3ZDQzMDA=",
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
                                         "display": "$4,800"
                                      },
                                      "id": "U2FsZUFydHdvcms6NWJjMTMxOTkwYWYwM2M3NDRiOTFlNTMy"
                                   },
                                   "is_inquireable": False,
                                   "id": "QXJ0d29yazo1YmMxMzE5NzBhYzZhNjAzNDVkMjEyMzA=",
                                   "is_saved": False,
                                   "is_biddable": False
                                }
                             },
                             {
                                "node": {
                                   "slug": "alphonse-mucha-job-22",
                                   "internalID": "5ddd55d152539a000ef8c6d3",
                                   "image": {
                                      "url": "https://d32dm0rphc51dk.cloudfront.net/nP1YQtAICPd8B5Hyt_L-7w/large.jpg",
                                      "aspectRatio": 0.67
                                   },
                                   "imageTitle": "Alphonse Mucha, ‘Job’, 1898",
                                   "title": "Job",
                                   "href": "/artwork/alphonse-mucha-job-22",
                                   "date": "1898",
                                   "sale_message": None,
                                   "cultural_maker": None,
                                   "artists": [
                                      {
                                         "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                         "href": "/artist/alphonse-mucha",
                                         "name": "Alphonse Mucha"
                                      }
                                   ],
                                   "collecting_institution": None,
                                   "partner": {
                                      "name": "Hindman",
                                      "href": "/auction/leslie-hindman-auctioneers",
                                      "id": "UGFydG5lcjo1YWU4YmUxMzhiM2I4MTdlZjEyNTI5Mjg=",
                                      "type": "Auction House"
                                   },
                                   "sale": {
                                      "is_auction": True,
                                      "is_closed": True,
                                      "id": "U2FsZTo1ZGQ4MmQyM2UwYTdkYzAwMTI5ZThhM2E=",
                                      "is_live_open": False,
                                      "is_open": False,
                                      "is_preview": False,
                                      "display_timely_at": None
                                   },
                                   "sale_artwork": {
                                      "counts": {
                                         "bidder_positions": 1
                                      },
                                      "highest_bid": {
                                         "display": "$1,500"
                                      },
                                      "opening_bid": {
                                         "display": "$1,500"
                                      },
                                      "id": "U2FsZUFydHdvcms6NWRkZDU1ZDg2NGVlM2YwMDBlM2JjZTkz"
                                   },
                                   "is_inquireable": False,
                                   "id": "QXJ0d29yazo1ZGRkNTVkMTUyNTM5YTAwMGVmOGM2ZDM=",
                                   "is_saved": False,
                                   "is_biddable": False
                                }
                             },
                             {
                                "node": {
                                   "slug": "alphonse-mucha-job-r-dot-slash-w-51",
                                   "internalID": "5ad62fd01a1e861674647987",
                                   "image": {
                                      "url": "https://d32dm0rphc51dk.cloudfront.net/j6DhgDcFZVX64bS-d_YwQA/large.jpg",
                                      "aspectRatio": 0.66
                                   },
                                   "imageTitle": "Alphonse Mucha, ‘Job (R./W. 51)’, 1898",
                                   "title": "Job (R./W. 51)",
                                   "href": "/artwork/alphonse-mucha-job-r-dot-slash-w-51",
                                   "date": "1898",
                                   "sale_message": None,
                                   "cultural_maker": None,
                                   "artists": [
                                      {
                                         "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                         "href": "/artist/alphonse-mucha",
                                         "name": "Alphonse Mucha"
                                      }
                                   ],
                                   "collecting_institution": None,
                                   "partner": {
                                      "name": "Doyle",
                                      "href": "/auction/partner-595e64cdcd530e765d529647",
                                      "id": "UGFydG5lcjo1OTVlNjRjZGNkNTMwZTc2NWQ1Mjk2NDc=",
                                      "type": "Auction House"
                                   },
                                   "sale": {
                                      "is_auction": True,
                                      "is_closed": True,
                                      "id": "U2FsZTo1YWQwZTAzYWNiNGMyNzE4NDdhNmYwY2E=",
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
                                         "display": "$1,500"
                                      },
                                      "id": "U2FsZUFydHdvcms6NWFkNjJmZDJjYjRjMjcxNDFlNWE1MmQw"
                                   },
                                   "is_inquireable": False,
                                   "id": "QXJ0d29yazo1YWQ2MmZkMDFhMWU4NjE2NzQ2NDc5ODc=",
                                   "is_saved": False,
                                   "is_biddable": False
                                }
                             },
                             {
                                "node": {
                                   "slug": "alphonse-mucha-job-poster-from-maxims-chicago",
                                   "internalID": "5a625795cd530e51721f2193",
                                   "image": {
                                      "url": "https://d32dm0rphc51dk.cloudfront.net/qhcaHomPZ6bTSE3YAEz2cw/large.jpg",
                                      "aspectRatio": 1
                                   },
                                   "imageTitle": "Alphonse Mucha, ‘Job poster from Maxim's, Chicago’, 1898",
                                   "title": "Job poster from Maxim's, Chicago",
                                   "href": "/artwork/alphonse-mucha-job-poster-from-maxims-chicago",
                                   "date": "1898",
                                   "sale_message": None,
                                   "cultural_maker": None,
                                   "artists": [
                                      {
                                         "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ==",
                                         "href": "/artist/alphonse-mucha",
                                         "name": "Alphonse Mucha"
                                      }
                                   ],
                                   "collecting_institution": None,
                                   "partner": {
                                      "name": "Rago/Wright",
                                      "href": "/auction/partner-595e69f6a09a671938435977",
                                      "id": "UGFydG5lcjo1OTVlNjlmNmEwOWE2NzE5Mzg0MzU5Nzc=",
                                      "type": "Auction House"
                                   },
                                   "sale": {
                                      "is_auction": True,
                                      "is_closed": True,
                                      "id": "U2FsZTo1YTYyMzE2ZDljMThkYjdiYTgyZDRiOWE=",
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
                                         "display": "$2,800"
                                      },
                                      "opening_bid": {
                                         "display": "$2,200"
                                      },
                                      "id": "U2FsZUFydHdvcms6NWE2MjU3OTdhMDlhNjcxNWZkNjM1MTFm"
                                   },
                                   "is_inquireable": False,
                                   "id": "QXJ0d29yazo1YTYyNTc5NWNkNTMwZTUxNzIxZjIxOTM=",
                                   "is_saved": False,
                                   "is_biddable": False
                                }
                             }
                          ],
                          "id": "ZmlsdGVyQXJ0d29ya3NDb25uZWN0aW9uOnsiYWdncmVnYXRpb25zIjpbInRvdGFsIl0sImFydGlzdF9zZXJpZXNfaWQiOiI3NjFjNWQ3YS04NWNjLTQ0ZjAtOWQyNy0yMTNlYWI0ZmUzYWEiLCJleGNsdWRlX2FydHdvcmtfaWRzIjpbIjVjYWJhMDk4ODc3NDg5NDFlZTdiMWRlMCJdLCJwYWdlIjoxLCJzaXplIjoyMCwic29ydCI6Ii1kZWNheWVkX21lcmNoIn0="
                       }
                    }
                 }
              ]
           },
           "seriesArtist": {
              "artistSeriesConnection": {
                 "edges": [
                    {
                       "node": {
                          "internalID": "f312bae3-f9d0-4259-871f-a0d4599a3f55",
                          "title": "Lorenzaccio",
                          "slug": "alphonse-mucha-lorenzaccio",
                          "featured": False,
                          "artworksCountMessage": "2 available",
                          "image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FH-x6cmA8HIiTQO9JTR51NA%2Flarge.jpg"
                             }
                          }
                       }
                    },
                    {
                       "node": {
                          "internalID": "cb81251b-b90d-4f14-9b8c-33b1131daadb",
                          "title": "Moët & Chandon",
                          "slug": "alphonse-mucha-moet-and-chandon",
                          "featured": False,
                          "artworksCountMessage": "2 available",
                          "image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FCBrNJiuuneh_Zm_TdIc6Yg%2Flarge.jpg"
                             }
                          }
                       }
                    },
                    {
                       "node": {
                          "internalID": "3c7388ef-d425-4077-92f6-64f7f21524b5",
                          "title": "Salon des Cents",
                          "slug": "alphonse-mucha-salon-des-cents",
                          "featured": False,
                          "artworksCountMessage": "2 available",
                          "image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FzVERnQ3TkrYJcokNH6K3yA%2Flarge.jpg"
                             }
                          }
                       }
                    },
                    {
                       "node": {
                          "internalID": "27214b0a-a5da-426c-a8d7-9facf72b1487",
                          "title": "Seasons",
                          "slug": "alphonse-mucha-seasons",
                          "featured": False,
                          "artworksCountMessage": "2 available",
                          "image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FMzMOn0ZxhKjaVkq54qQ8Hg%2Flarge.jpg"
                             }
                          }
                       }
                    },
                    {
                       "node": {
                          "internalID": "761c5d7a-85cc-44f0-9d27-213eab4fe3aa",
                          "title": "Job",
                          "slug": "alphonse-mucha-job",
                          "featured": False,
                          "artworksCountMessage": "1 available",
                          "image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FeLndsQDFY_lb6FkaAkt7nA%2Flarge.jpg"
                             }
                          }
                       }
                    },
                    {
                       "node": {
                          "internalID": "8582d221-3b68-4173-a2bb-3e1980c53d0e",
                          "title": "Biscuits",
                          "slug": "alphonse-mucha-biscuits",
                          "featured": False,
                          "artworksCountMessage": "1 available",
                          "image": {
                             "cropped": {
                                "url": "https://d7hftxdivxxvm.cloudfront.net?resize_to=fill&width=320&height=320&quality=80&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FZROpbxzCrq8QhM0f6zx6qw%2Flarge.jpg"
                             }
                          }
                       }
                    }
                 ]
              },
              "id": "QXJ0aXN0OjRmYmFiYzk5OGIzMTM3MDAwMTAwMDZkYQ=="
           },
           "seriesForCounts": {
              "edges": [
                 {
                    "node": {
                       "artworksCount": 9
                    }
                 }
              ]
           },
           "pricingContext": {
              "appliedFiltersDisplay": "Price ranges of small prints by Alphonse Mucha",
              "appliedFilters": {
                 "dimension": "SMALL",
                 "category": "PRINT"
              },
              "bins": [
                 {
                    "maxPrice": "$1,050",
                    "maxPriceCents": 105000,
                    "minPrice": "$700",
                    "minPriceCents": 70000,
                    "numArtworks": 3
                 },
                 {
                    "maxPrice": "$1,400",
                    "maxPriceCents": 140000,
                    "minPrice": "$1,050",
                    "minPriceCents": 105000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$1,750",
                    "maxPriceCents": 175000,
                    "minPrice": "$1,400",
                    "minPriceCents": 140000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$2,100",
                    "maxPriceCents": 210000,
                    "minPrice": "$1,750",
                    "minPriceCents": 175000,
                    "numArtworks": 1
                 },
                 {
                    "maxPrice": "$2,450",
                    "maxPriceCents": 245000,
                    "minPrice": "$2,100",
                    "minPriceCents": 210000,
                    "numArtworks": 1
                 },
                 {
                    "maxPrice": "$2,800",
                    "maxPriceCents": 280000,
                    "minPrice": "$2,450",
                    "minPriceCents": 245000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$3,150",
                    "maxPriceCents": 315000,
                    "minPrice": "$2,800",
                    "minPriceCents": 280000,
                    "numArtworks": 4
                 },
                 {
                    "maxPrice": "$3,500",
                    "maxPriceCents": 350000,
                    "minPrice": "$3,150",
                    "minPriceCents": 315000,
                    "numArtworks": 1
                 },
                 {
                    "maxPrice": "$3,850",
                    "maxPriceCents": 385000,
                    "minPrice": "$3,500",
                    "minPriceCents": 350000,
                    "numArtworks": 3
                 },
                 {
                    "maxPrice": "$4,200",
                    "maxPriceCents": 420000,
                    "minPrice": "$3,850",
                    "minPriceCents": 385000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$4,550",
                    "maxPriceCents": 455000,
                    "minPrice": "$4,200",
                    "minPriceCents": 420000,
                    "numArtworks": 1
                 },
                 {
                    "maxPrice": "$4,900",
                    "maxPriceCents": 490000,
                    "minPrice": "$4,550",
                    "minPriceCents": 455000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$5,250",
                    "maxPriceCents": 525000,
                    "minPrice": "$4,900",
                    "minPriceCents": 490000,
                    "numArtworks": 4
                 },
                 {
                    "maxPrice": "$5,600",
                    "maxPriceCents": 560000,
                    "minPrice": "$5,250",
                    "minPriceCents": 525000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$5,950",
                    "maxPriceCents": 595000,
                    "minPrice": "$5,600",
                    "minPriceCents": 560000,
                    "numArtworks": 2
                 },
                 {
                    "maxPrice": "$6,300",
                    "maxPriceCents": 630000,
                    "minPrice": "$5,950",
                    "minPriceCents": 595000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$6,650",
                    "maxPriceCents": 665000,
                    "minPrice": "$6,300",
                    "minPriceCents": 630000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$7,000",
                    "maxPriceCents": 700000,
                    "minPrice": "$6,650",
                    "minPriceCents": 665000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$7,350",
                    "maxPriceCents": 735000,
                    "minPrice": "$7,000",
                    "minPriceCents": 700000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$7,700",
                    "maxPriceCents": 770000,
                    "minPrice": "$7,350",
                    "minPriceCents": 735000,
                    "numArtworks": 0
                 },
                 {
                    "maxPrice": "$8,050",
                    "maxPriceCents": 805000,
                    "minPrice": "$7,700",
                    "minPriceCents": 770000,
                    "numArtworks": 1
                 }
              ]
           }
        },
        "me": None
     }
  }
]
print(len(mucha[0]))
print(mucha[0]["data"]["artwork"]["images"][0]["url"])
