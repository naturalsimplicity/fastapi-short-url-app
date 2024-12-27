FROM python:3.12-slim

COPY . shorturl

WORKDIR shorturl

RUN pip install -r requirements.txt

EXPOSE 80

VOLUME /app/data

ENV PYTHONUNBUFFERED=1

CMD uvicorn shorturl.main:app --host 0.0.0.0 --port 80
