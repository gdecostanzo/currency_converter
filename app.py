# 3th parts imports
from flask import (
    Flask,
    request,
    jsonify
)
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# internal imports
import currency_parser
from static.convert_schema import convert_schema

app = Flask(__name__)
exchange_rates_by_data = currency_parser.load_currencies()


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
        validate(request.args.to_dict(), convert_schema)
    except ValidationError as ve:
        return ve.message, 400

    # Get parameters
    amount = float(request.args.get('amount'))
    src_currency = request.args.get('src_currency')
    dest_currency = request.args.get('dest_currency')
    # if not specified, latest date available will be used
    reference_date = request.args.get('reference_date', list(exchange_rates_by_data.keys())[0])
    if reference_date not in exchange_rates_by_data:
        return "Reference date not found", 404

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
