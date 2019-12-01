# currency_converter
This is a simple online currency converter, made with Python Flask.

The Web API exposes an endpoint called ​c​onvert.
It accepts the following parameters:

- **amount** (mandatory): the amount to convert (e.g. 12.35)
- **src​_currency** (mandatory): ISO currency code for the source currency to convert (e.g. EUR,
USD, GBP)
- **dest_currency** (mandatory): ISO currency code for the destination currency to convert (e.g. EUR,
USD, GBP)
- **re​ference_date** (optional): reference date for the exchange rate, in YYYY-MM-DD format. 
If not provided, the latest date available will be used

An example of usage:
```
/convert?amount=10&src_currency=EUR&dest_currency=GBP
```

An example of response:
```
{
    “amount”: 8.518,
    “currency”: ”EUR”
}
```


### Installing dependencies
```
pipenv install
```

##### Dev dependencies for unit testing
```
pipenv install --dev
```

### Run application
```
pipenv run python app.py
```

### Run tests
```
pytest tests
```

## Docker
To build docker image:
```
docker build -t currency_converter:latest .
```

To run docker container:
```
docker run -d -p 80:80 currency_converter:latest
```