FROM python:3.9-slim

RUN mkdir /app

RUN python3 -m venv .venv

COPY requirements.txt .

RUN .venv/bin/pip install -Ur requirements.txt

COPY src src
COPY .env .
COPY tools/deploy.sh deploy.sh

RUN ["chmod", "+x", "./deploy.sh"]

CMD ["/bin/bash", "./deploy.sh"]
