FROM python:3.10.14-alpine3.18

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD [ "python", "app.py" ]

EXPOSE 5000