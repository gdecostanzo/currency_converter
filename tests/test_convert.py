# Python imports
import os
import sys

# 3th parts imports
from flask import json
import requests_mock


_dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _dir_path + '/../')

with open(os.path.join(_dir_path, 'eurofxref-hist-90d.xml')) as f:
    file_text = f.read()


def test_success():
    with requests_mock.Mocker() as mock_request:
        mock_request.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml', text=file_text)
        from app import app
        response = app.test_client().get('/convert?amount=10&src_currency=EUR&des​t_currency=GBP&reference_date=2019-11-28')

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200

    assert 'amount' in data
    assert data['amount'] == 8.52

    assert 'currency' in data
    assert data['currency'] == 'GBP'


def test_bad_request():
    # Test invalid amount
    with requests_mock.Mocker() as mock_request:
        mock_request.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml', text=file_text)
        from app import app
        response = app.test_client().get('/convert?amount=10.a&src_currency=EUR&des​t_currency=GBP&reference_date=2019-11-28')

        assert response.status_code == 400
        assert response.get_data(as_text=True) == "Invalid amount value"

    # Test invalid currency code
    with requests_mock.Mocker() as mock_request:
        mock_request.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml', text=file_text)
        from app import app
        response = app.test_client().get(
            '/convert?amount=10&src_currency=EURO&des​t_currency=GBP&reference_date=2019-11-28')

        assert response.status_code == 400
        assert response.get_data(as_text=True) == "Invalid src_currency code"

    # Test invalid reference date
    with requests_mock.Mocker() as mock_request:
        mock_request.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml', text=file_text)
        from app import app
        response = app.test_client().get(
            '/convert?amount=10&src_currency=EUR&des​t_currency=GBP&reference_date=2019-11-008')

        assert response.status_code == 400
        assert response.get_data(as_text=True) == "Invalid reference date"


def test_not_found():
    # Test invalid amount
    with requests_mock.Mocker() as mock_request:
        mock_request.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml', text=file_text)
        from app import app
        response = app.test_client().get('/convert?amount=10&src_currency=EUR&des​t_currency=GBP&reference_date=2019-12-28')

        assert response.status_code == 404
        assert response.get_data(as_text=True) == "Reference date not available"