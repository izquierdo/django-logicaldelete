from django.test import TestCase
from logicaldelete.tests.models import Author, Book


class RelatedGetTestCase(TestCase):
    def test_related_get(self):
        """
        Test that we don't break querying related objects.

        """
        author = Author.objects.create()

        book_by_author = Book.objects.create(title='book 0')
        book_no_author = Book.objects.create(title='book 1')

        author.books.add(book_by_author)

        self.assertEqual(author.books.get().title, 'book 0')
