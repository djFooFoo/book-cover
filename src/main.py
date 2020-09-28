import io

import fastapi
import requests
from fastapi import HTTPException
from starlette.responses import StreamingResponse

from book_cover import BookCover

bookCover = BookCover(requests)
app = fastapi.FastAPI()


@app.get("/books/{isbn}")
async def get_book_cover(isbn: str):
    print(f'Retrieving image via isbn `{isbn}`')
    img = None
    try:
        img = bookCover.get_by(isbn)
    except RuntimeError as error:
        print(error)
        raise HTTPException(status_code=404, detail=f'Image with isbn `{isbn}` not found')
    return StreamingResponse(io.BytesIO(img), media_type="image/jpg")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)
