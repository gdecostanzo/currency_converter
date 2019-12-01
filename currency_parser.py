# Python imports
from xml.dom import minidom

# 3th parts imports
import requests


def load_currencies() -> dict:
    """Read latest currency rates (EUR) from Web and returns a dictionary.

    An example of dict returned:
    {
        "2019-11-28": {
            "USD": "1.1005",
            "JPY": "120.5",
            ...
        },
        ....
    }

    :return: (dict)
    """

    response = requests.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml')
    doc = minidom.parseString(response.text)

    exchange_rates_by_data = dict()
    cubes = doc.getElementsByTagName('Cube')

    for cube in cubes:
        if cube.hasAttribute('time'):
            exchange_rates = {'EUR': '1.0'}
            for elem in cube.childNodes:
                exchange_rates[elem.getAttribute('currency')] = elem.getAttribute('rate')

            exchange_rates_by_data[cube.getAttribute('time')] = exchange_rates

    return exchange_rates_by_data

