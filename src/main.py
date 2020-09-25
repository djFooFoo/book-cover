import base64
import fastapi
import requests
from fastapi import HTTPException

import book_cover

bookCover = book_cover.BookCover(requests)
app = fastapi.FastAPI()


@app.get("/book-cover/{isbn}")
async def get_book_cover(isbn: str):
    print(f'Retrieving image via isbn `{isbn}`')
    img = None
    try:
        img = bookCover.get_by(isbn)
    except RuntimeError as error:
        print(error)
        raise HTTPException(status_code=404, detail=f'Image with isbn `{isbn}` not found')
    return base64.b64encode(img), 200


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)
