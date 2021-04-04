# German - English Dictionary REST API

Searches over 300.000 words and phrases.  
Search in either German or English.  
Built with Python and Flask.  
Hosted on Google App Engine.  

## API Documentation
Base Url for requests: `https://german-english-dictionary-api.uc.r.appspot.com/`

## Endpoints
GET `/translate` Translate a word or a phrase
Query Parameters:
- `term` - mandatory, german or english string that will be translated
- `limit` - optional, results limit (default=100)
- `page` - optional, page for offseting results(default=0)

## Example
`/translate?term=thanks&limit=1`

Response:
```
{
    "search_term": "thanks",
    "count": 43,
    "limit": 1,
    "page": 0,
    "has_more": true,
    "results": [
        {
            "german": {
                "term": "danke {interj}",
                "examples": [
                    "Danke!",
                    "Danke schön!; Danke sehr!",
                    "Nein danke!; Danke, nein!",
                    "Danke im Voraus!",
                    "Danke gleichfalls!",
                    "Danke für Ihren Auftrag.",
                    "Danke für Ihre Hilfe.",
                    "Danke für Ihr Verständnis.",
                    "Danke für Ihr Vertrauen in uns.",
                    "Danke für Ihre Zusammenarbeit.",
                    "Danke, dass Sie sich Zeit genommen haben.",
                    "Danke für Ihre Bestellung.",
                    "Danke der Nachfrage."
                ]
            },
            "english": {
                "term": "thanks; ta [Br.] [coll.] /tnx/ /thx/",
                "examples": [
                    "Thank you! Thanks!; Thanx!",
                    "Thank you very much!; Cheers! [Br.]",
                    "No, thanks!",
                    "Thanks in advance! /TIA/",
                    "Thank you, the same to you!",
                    "Thank you for placing your order with us.",
                    "Thank you for your help.; Thanks for your help.",
                    "Thank you for your understanding.",
                    "Thank you for having placed your trust in us.",
                    "Thank you for your cooperation.",
                    "Thank you for your time.",
                    "Thanks for your order.",
                    "Thank you for asking."
                ]
            }
        }
    ]
}
```

