convert_schema = {
    "type": "object",
    "properties": {
        "amount": {
            "type": "string",
            "pattern": "^[0-9]+(\\.[0-9][0-9]?)?$",
          },

        "src_currency" : {
            "type": "string",
            "enum": ["EUR", "USD", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK",
                     "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR",
                     "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"]
          },

        "dest_currency" : {
            "type": "string",
            "enum": ["EUR", "USD", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK",
                     "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR",
                     "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"]

          },

        "reference_date": {
          "type": "string",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
          }
    },
    "required": ["amount", "src_currency", "dest_currency"],
    "additionalProperties": False
}