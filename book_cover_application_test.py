import unittest

import requests


class BookCoverApplicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.uuid = '0743269519'
        self.url = f"http://0.0.0.0:10000/book-cover/{self.uuid}"
        self.response: requests.Response = requests.get(url=self.url)

    def test_returns_ok(self) -> None:
        self.assertEqual(200, self.response.status_code)

    def test_returns_header_application_pdf(self) -> None:
        self.assertEqual('image/jpeg', self.response.headers['content-type'])

    def test_returns_string(self) -> None:
        self.assertIsInstance(self.response.content, bytes)


if __name__ == "__main__":
    unittest.main()
