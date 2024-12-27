# FastAPI ToDo app

FastAPI Short URL App for Mentors Seminar Course

## Features

Service provide short IDs for URLS of any length 

To create short ID you need to:
1. `POST /api/v1/urls/shorten` — creates short ID for your URL. Further requests
with the same URL will return the same short ID

Get full URL using short ID:
1. `GET /api/v1/urls/stats/{short_id}` — returns info
with both short ID and full URL
2. `GET /api/v1/urls/{short_id}` — redirects user to full URL

## Application startup

Create an image from Dockerfile:

    docker build -t shorturl-service .

Create volume for the app data:

    docker volume create shorturl_data

Start container with the app:
    
    docker run --name shorturl-service -d -p 8001:80 -v shorturl_data:/app/data shorturl-service
