FROM python:3.8-alpine

WORKDIR /app

# Create the environment:
COPY . .
RUN apt-get update && pip install -r requirements.txt
EXPOSE 10000

CMD book_cover_application