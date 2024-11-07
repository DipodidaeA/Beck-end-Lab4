FROM python:3.11.3-slim-bullseye


WORKDIR /app


COPY requirements.txt .


RUN python -m pip install -r requirements.txt


COPY . /app


ENV FLASK_APP=__init__.py


RUN flask db init


CMD flask db migrate && flask db upgrade && flask --app __init__ run -h 0.0.0.0 -p 5003