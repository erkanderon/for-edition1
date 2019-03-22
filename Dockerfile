FROM python:3.7-alpine
MAINTAINER erkanderon

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /univer
WORKDIR /univer
COPY ./univer /univer


RUN adduser -D dockerderon
USER dockerderon