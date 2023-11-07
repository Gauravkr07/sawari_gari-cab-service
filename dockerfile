FROM python:3.8-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV SECRET_KEY=

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libpq-dev gcc python3-dev  python3-wheel python3-setuptools libenchant-2-2

RUN pip install wheel
RUN pip install -r requirements.txt

ADD . /app/

EXPOSE 8000

CMD gunicorn -b '0.0.0.0:8000' sawari_gari.asgi -w 2 -k uvicorn.workers.UvicornWorker 