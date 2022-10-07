FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt install libpq-dev
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -v -r requirements.txt
EXPOSE 8000  
