from django.test import TestCase
from rest_framework.test import APIClient
from .models import Author, Book


class TestModel(TestCase):
    def setUp(self):
        self.apiClient = APIClient()
        self.basePathAuthor = "/api/Author/"
        self.basePathBook = "/api/Book/"

        self.testAuthor = Author.objects.create(name="testAuthor")

    def test_create_author_with_same_name(self):
        response = self.apiClient.post(self.basePathAuthor, {"name": "testAuthor"})

        self.assertTrue(
            response.status_code != 201, "Name of the authors should be unique!"
        )

    def test_str_name_is_equal_to_name(self):
        self.assertTrue(self.testAuthor.name == str(self.testAuthor))

    def test_create_book_without_title(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "isbn": "test",
                "author": [1],
                "published_by": "TestPublish",
                "book_edition": "TestEdition",
                "pages": 10,
                "description": "TestDescription",
            },
        )

        self.assertTrue(response.status_code != 201, "Name should be required!")

    def test_create_book_without_isbn(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "test",
                "author": [1],
                "published_by": "TestPublish",
                "book_edition": "TestEdition",
                "pages": 10,
                "description": "TestDescription",
            },
        )

        self.assertTrue(response.status_code != 201, "ISBN should be required!")

    def test_create_book_without_author(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "TestBook",
                "isbn": "test",
                "published_by": "TestPublish",
                "book_edition": "TestEdition",
                "pages": 10,
                "description": "TestDescription",
            },
        )
        self.assertTrue(response.status_code != 201, "Author should be required!")

    def test_create_book_without_published_by(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "TestBook",
                "isbn": "test",
                "author": [1],
                "book_edition": "TestEdition",
                "pages": 10,
                "description": "TestDescription",
            },
        )

        self.assertTrue(
            response.status_code != 201, "Published_by field should be required!"
        )

    def test_create_book_without_book_edition(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "TestBook",
                "isbn": "test",
                "author": [1],
                "published_by": "TestPublish",
                "pages": 10,
                "description": "TestDescription",
            },
        )

        self.assertTrue(
            response.status_code != 201, "Book_edition field should be required!"
        )

    def test_create_book_without_pages(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "TestBook",
                "isbn": "test",
                "author": [1],
                "published_by": "TestPublish",
                "book_edition": "TestEdition",
                "description": "TestDescription",
            },
        )

        self.assertTrue(response.status_code != 201, "Pages field should be required!")

    def test_create_book_without_description(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "TestBook",
                "isbn": "test",
                "author": [1],
                "published_by": "TestPublish",
                "book_edition": "TestEdition",
                "pages": 10,
            },
        )

        self.assertTrue(response.status_code != 201, "Description should be required!")

    def test_create_book_with_three_authors(self):
        for num in range(2):
            Author.objects.create(name=f"Test Author {num}")
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "TestBook",
                "isbn": "test",
                "author": [1, 2, 3],
                "published_by": "TestPublish",
                "book_edition": "TestEdition",
                "pages": 10,
                "description": "TestDescription",
            },
        )

        self.assertTrue(
            response.status_code == 201,
            "Book should be able to receive more than one author.",
        )

    def test_create_book_with_negative_pages(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "TestBook",
                "isbn": "test",
                "author": [1],
                "published_by": "TestPublish",
                "book_edition": "TestEdition",
                "pages": -10,
                "description": "TestDescription",
            },
        )

        self.assertTrue(
            response.status_code != 201, "Book should have a least one page."
        )

    def test_create_book_with_zero_pages(self):
        response = self.apiClient.post(
            self.basePathBook,
            {
                "title": "TestBook",
                "isbn": "test",
                "author": [1],
                "published_by": "TestPublish",
                "book_edition": "TestEdition",
                "pages": 0,
                "description": "TestDescription",
            },
        )

        self.assertTrue(
            response.status_code != 201, "Book should have a least one page."
        )
