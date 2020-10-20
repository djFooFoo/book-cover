import base64

import requests


class BookCover:
    def __init__(self, request_library=requests):
        self.request_library = request_library

    def get_by(self, isbn: str) -> bytes:
        internal_url = f'http://www.dieterjordens.be:10003/images/{isbn}'
        book_result_internal_library = self.request_library.get(internal_url)
        print(book_result_internal_library.status_code)
        if book_result_internal_library.status_code == 200:
            return base64.decodebytes(book_result_internal_library.content)

        external_url = f'http://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false'
        book_result_external_library = self.request_library.get(external_url)
        print(book_result_external_library.status_code)
        if book_result_external_library.status_code == 200:
            image = book_result_external_library.content
            self.add_image(image, isbn)
            return image
        else:
            raise RuntimeError(f'No image found for the following isbn number: `{isbn}`')

    def add_image(self, image, isbn):
        image_data = {
            'id': isbn,
            'base64String': base64.b64encode(image).decode('utf-8')
        }
        print(self.request_library.post(url='http://www.dieterjordens.be:10003/images/', json=image_data))
