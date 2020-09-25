FROM python:3.8

RUN apt-get update

RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY src .
EXPOSE 10000
ENTRYPOINT [ "python", "main.py"]