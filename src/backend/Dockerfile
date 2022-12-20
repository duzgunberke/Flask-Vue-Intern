# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install python-dotenv


COPY . .

CMD [ "python", "main.py"]