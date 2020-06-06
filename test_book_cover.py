import unittest
from unittest import mock
from unittest.mock import Mock, mock_open

from mockito import when, verify

from book_cover import BookCover


class ResponseStub:
    def __init__(self, code: int, content: bytes = b'a series of bytes'):
        self.status_code = code
        self.content = content


class BookCoverApplicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.requestsMock = Mock()
        self.book_cover = BookCover(self.requestsMock)

    def test_retrievesBookCoverFromExternalSource(self) -> None:
        isbn = 'imaginary_isbn'
        url = f'http://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false'
        content = b'book content'
        when(self.requestsMock).get(url).thenReturn(ResponseStub(code=200, content=content))

        with mock.patch('os.walk'):
            with mock.patch('builtins.open', mock_open(), create=True):
                self.book_cover.get_by(isbn)

        verify(self.requestsMock).get(url)

    def test_writesBookCoverToBooksFolder(self) -> None:
        isbn = 'imaginary_isbn'
        url = f'http://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false'
        content = b'book content'
        when(self.requestsMock).get(url).thenReturn(ResponseStub(code=200, content=content))

        with mock.patch('os.walk'):
            with mock.patch('builtins.open', mock_open(), create=True) as mock_file_handle:
                self.book_cover.get_by(isbn)

        mock_file_handle.assert_called_with(f'books/{isbn}.jpg', 'wb')
        mock_file_handle().write.assert_called_once_with(content)

    def test_prefersBookCoverFromFileSystemOverExternalResource(self) -> None:
        isbn = 'imaginary_isbn'
        content = b'book content'

        with mock.patch('os.walk') as mock_walk:
            mock_walk.return_value = [('books', (), (f'{isbn}.jpg',))]
            with mock.patch('builtins.open', mock.mock_open(read_data=content)):
                book = self.book_cover.get_by(isbn)

        self.assertEqual(book, content)

    def test_throwsRuntimeExceptionWhenBookNotFound(self) -> None:
        isbn = 'imaginary_isbn'
        url = f'http://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false'

        response = ResponseStub(code=404)
        when(self.requestsMock).get(url).thenReturn(response)

        with self.assertRaises(Exception) as context:
            self.book_cover.get_by(isbn)

        self.assertRaises(RuntimeError)
        self.assertEqual(str(context.exception), f'No image found for the following isbn number: `{isbn}`.')


if __name__ == "__main__":
    unittest.main()
