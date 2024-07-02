FROM python:3.10.14-alpine3.18

WORKDIR /app

COPY requirements.txt .

RUN apk add git
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY wsgi.py .
COPY config.py .
COPY application application

CMD [ "python", "wsgi.py" ]

EXPOSE 5000