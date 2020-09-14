import unittest

import requests


class BookCoverApplicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.uuid = '9780062803832'
        self.url = f"http://www.dieterjordens.be:10000/book-cover/{self.uuid}"
        self.response: requests.Response = requests.get(url=self.url)

    def test_returns_ok(self) -> None:
        self.assertEqual(200, self.response.status_code)

    def test_returns_header_text_html_utf8(self) -> None:
        self.assertEqual('text/html; charset=utf-8', self.response.headers['content-type'])

    def test_returns_string(self) -> None:
        self.assertIsInstance(self.response.content, bytes)


if __name__ == "__main__":
    unittest.main()
