FROM python:3.8-alpine

ADD main.py /
ADD user.py /
ADD mock_datastore.py /
ADD requirements.txt /

RUN pip install -r /requirements.txt 

CMD [ "flask", "run", "/main.py" ]
EXPOSE 5000/tcp
