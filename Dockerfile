FROM python:3.6.4

WORKDIR /app

ENV PYTHONBUFFERED 1

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations

RUN python manage.py migrate
