FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /home/restapi
WORKDIR /home/restapi
COPY requirements.txt /home/restapi/
RUN pip install -r requirements.txt
COPY . /home/restapi/
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
