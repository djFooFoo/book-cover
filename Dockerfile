FROM python:3.8

COPY requirements.txt /tmp/

RUN apt-get update && pip install -r /tmp/requirements.txt

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

COPY . .
EXPOSE 10000
ENTRYPOINT [ "python", "./book_cover_application.py"]