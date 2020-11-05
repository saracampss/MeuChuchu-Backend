FROM python:3.7-buster

WORKDIR /meuchuchu
COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN apt update

CMD python3 app.py
