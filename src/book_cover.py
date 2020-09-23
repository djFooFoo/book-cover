import os


class BookCover:
    def __init__(self, request_library):
        self.request_library = request_library

    @staticmethod
    def file_exists(isbn: str) -> bool:
        for _, _, files in os.walk("../books"):
            for filename in files:
                if filename == f'{isbn}.jpg':
                    return True
        return False

    def get_by(self, isbn: str) -> bytes:
        if self.file_exists(isbn):
            with open(f"books/{isbn}.jpg", "rb") as read_file:
                return read_file.read()
        else:
            url = f'http://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false'
            result = self.request_library.get(url)
            if result.status_code == 200:
                content = result.content
                with open(f"books/{isbn}.jpg", "wb") as write_file:
                    write_file.write(content)
                return content
            raise RuntimeError(f'No image found for the following isbn number: `{isbn}`.')
