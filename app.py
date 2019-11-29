# Python imports
import re

# 3th parts imports
from flask import (
    Flask,
    request,
    jsonify
)

# internal imports
import parser

app = Flask(__name__)
exchange_rates_by_data = parser.load_currencies()
valid_iso_currency_codes = ('EUR', 'USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK',
                            'NOK', 'HRK', 'RUB', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW',
                            'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR')


@app.route('/convert')
def convert():
    """
    Converts the pr​ovided `amount` from​ `​src_currency` to `​​dest_currency`,
    given the exchange rate at the `​reference_date`.
    Returns a json with the converted amount.

    An example of call:
    /convert?amount=10&src_currency=EUR&des​t_currency=GBP&reference_date=2019-11-28

    An example of response:
    {
        “amount”: 8.518,
        “currency”: ”EUR”
    }

    :return: (str) a json string
    """

    # Parameters validation
    try:
        amount = float(request.args.get('amount'))
    except ValueError:
        return "Invalid amount value", 400

    src_currency = request.args.get('src_currency')
    dest_currency = request.args.get('des​t_currency')
    if src_currency not in valid_iso_currency_codes:
        return "Invalid src_currency code", 400
    if dest_currency not in valid_iso_currency_codes:
        return "Invalid dest_currency code", 400

    # if not specified, latest date available will be used
    reference_date = request.args.get('reference_date', list(exchange_rates_by_data.keys())[0])
    if not re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}$', reference_date):
        return "Invalid reference date", 400
    if reference_date not in exchange_rates_by_data:
        return "Reference date not available", 404

    # Convert amount
    src_rate = float(exchange_rates_by_data[reference_date][src_currency])
    dest_rate = float(exchange_rates_by_data[reference_date][dest_currency])
    converted_amount = amount / src_rate * dest_rate

    response = {
        "amount": round(converted_amount, 2),
        "currency": dest_currency
    }

    return jsonify(response)


if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)
