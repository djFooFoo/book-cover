# book-cover
A wrapper for a book service API that caches book covers. This prevents getting blocked from a free API because of doing the same requests over and over again.


## Building docker image (build & run)

docker container build -t book-cover .
docker container run --restart unless-stopped -v $(pwd)/books:/app/books -p 10000:10000 --name book-cover -d book-cover
