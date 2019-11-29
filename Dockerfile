from python:3.7

WORKDIR /usr/src/app

ADD . .

RUN pip install pipenv
RUN pipenv install --system --deploy

ENTRYPOINT python app.py