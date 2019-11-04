FROM python:3.8-alpine

ADD app.py /
ADD user.yaml /
ADD requirements.txt /

RUN apk add build-base
RUN pip install -r /requirements.txt 

CMD [ "python", "/app.py" ]
EXPOSE 8080/tcp
