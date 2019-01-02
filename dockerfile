FROM python:3

ADD runcode.py /

CMD [ "python", "./runcode.py" ]