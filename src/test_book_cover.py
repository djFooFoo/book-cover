import unittest
from unittest import mock
from unittest.mock import Mock, mock_open

from mockito import when, verify

from src import book_cover


class ResponseStub:
    def __init__(self, code: int, content: bytes = b'a series of bytes'):
        self.status_code = code
        self.content = content


class BookCoverApplicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.requests_mock = Mock()
        self.book_cover = book_cover.BookCover(self.requests_mock)

    def test_retrieves_book_cover_from_external_source(self) -> None:
        isbn = 'imaginary_isbn'
        url = f'http://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false'
        content = b'book content'
        when(self.requests_mock).get(url).thenReturn(ResponseStub(code=200, content=content))

        with mock.patch('os.walk'):
            with mock.patch('builtins.open', mock_open(), create=True):
                self.book_cover.get_by(isbn)

        verify(self.requests_mock).get(url)

    def test_writes_book_cover_to_books_folder(self) -> None:
        isbn = 'imaginary_isbn'
        url = f'http://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false'
        content = b'book content'
        when(self.requests_mock).get(url).thenReturn(ResponseStub(code=200, content=content))

        with mock.patch('os.walk'):
            with mock.patch('builtins.open', mock_open(), create=True) as mock_file_handle:
                self.book_cover.get_by(isbn)

        mock_file_handle.assert_called_with(f'books/{isbn}.jpg', 'wb')
        mock_file_handle().write.assert_called_once_with(content)

    def test_prefers_book_cover_from_file_system_over_external_resource(self) -> None:
        isbn = 'imaginary_isbn'
        content = b'book content'

        with mock.patch('os.walk') as mock_walk:
            mock_walk.return_value = [('books', (), (f'{isbn}.jpg',))]
            with mock.patch('builtins.open', mock.mock_open(read_data=content)):
                book = self.book_cover.get_by(isbn)

        self.assertEqual(book, content)

    def test_throws_runtime_exception_when_book_not_found(self) -> None:
        isbn = 'imaginary_isbn'
        url = f'http://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false'

        response = ResponseStub(code=404)
        when(self.requests_mock).get(url).thenReturn(response)

        with self.assertRaises(Exception) as context:
            self.book_cover.get_by(isbn)

        self.assertRaises(RuntimeError)
        self.assertEqual(str(context.exception), f'No image found for the following isbn number: `{isbn}`.')


if __name__ == "__main__":
    unittest.main()
