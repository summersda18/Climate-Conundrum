# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .
RUN sed -i 's/DEBUG = False/DEBUG = True/g' ./climate_conundrum/settings.py \
    && sed -i "s/'default'/'develop'/g" ./climate_conundrum/settings.py \
    && sed -i "s/'production'/'default'/g" ./climate_conundrum/settings.py \
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt
CMD python3 manage.py runserver 0.0.0.0:8080
