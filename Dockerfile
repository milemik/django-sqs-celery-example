FROM python:3.10.0-slim-bullseye

ENV PYTHONUNBUFFERED=1
RUN apt update
RUN apt-get install libssl-dev libcurl4-openssl-dev python-dev gcc -y

RUN pip install --upgrade pip && pip install poetry

COPY . /app
WORKDIR /app

RUN poetry export --without-hashes -f requirements.txt --output requirements.txt && pip install -r requirements.txt
RUN echo pip freeze
