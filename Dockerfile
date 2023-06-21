FROM python:3.8.10-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# Install python and postgres dependencies under a virtual package
RUN pip install --upgrade pip -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./ /app

COPY ./run_web.sh /bin/run_web.sh
RUN chmod 777 -R /bin/run_web.sh

COPY ./run_celery_worker.sh /bin/run_celery_worker.sh
RUN chmod 777 -R /bin/run_celery_worker.sh

COPY ./create_rabbit_credentials.sh /bin/create_rabbit_credentials.sh
RUN chmod 777 -R /bin/create_rabbit_credentials.sh