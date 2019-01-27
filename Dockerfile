FROM python:3.6

WORKDIR /underworld

ADD . /underworld

RUN pip install --no-cache-dir -r requirements.txt
