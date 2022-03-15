# syntax=docker/dockerfile:1

FROM python:3.8.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD [ "python3", "app.py"]
