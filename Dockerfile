FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY . .
RUN apt-get update && conda env create -f environment.yml
EXPOSE 10000

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "-n", "book-cover", "python", "book_cover_application.py"]