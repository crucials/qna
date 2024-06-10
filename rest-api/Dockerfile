FROM python:3.10.14-slim

WORKDIR /qna-rest-api

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "./src/main.py" ]
