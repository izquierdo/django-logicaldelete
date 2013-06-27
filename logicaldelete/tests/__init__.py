from django.test import TestCase
from logicaldelete.tests.models import Author, Book


class LogicalDeletedManagerTestCase(TestCase):
    def test_get_query_set(self):
        book = Book.objects.create()
        deleted_book = Book.objects.create()

        deleted_book.delete()

        self.assertEqual(list(Book.objects.get_query_set()), [book])

    def test_get(self):
        book = Book.objects.create()

        self.assertEqual(Book.objects.get(), book)

    def test_get_deleted(self):
        deleted_book = Book.objects.create()
        deleted_book.delete()

        self.assertEqual(Book.objects.get(), deleted_book)

    def test_everything(self):
        book = Book.objects.create(title='a')
        deleted_book = Book.objects.create(title='b')

        deleted_book.delete()

        self.assertEqual(list(Book.objects.everything().order_by('title')),
                         [book, deleted_book])

    def test_only_deleted(self):
        book = Book.objects.create(title='a')
        deleted_book = Book.objects.create(title='b')

        deleted_book.delete()

        self.assertEqual(list(Book.objects.only_deleted()), [deleted_book])

    def test_filter(self):
        book_a_0 = Book.objects.create(title='a')
        book_a_1 = Book.objects.create(title='a')
        book_a_deleted = Book.objects.create(title='a')
        book_b = Book.objects.create(title='b')

        book_a_deleted.delete()

        self.assertEqual(Book.objects.filter(title='a').count(), 2)

    def test_filter_with_pk(self):
        book_a_0 = Book.objects.create(title='a')
        book_a_1 = Book.objects.create(title='a')
        book_a_deleted = Book.objects.create(title='a')
        book_b = Book.objects.create(title='b')

        book_a_deleted.delete()

        self.assertEqual(list(Book.objects.filter(pk=book_a_deleted.pk)),
                         [book_a_deleted])


class RelatedGetTestCase(TestCase):
    def test_related_get(self):
        """
        Don't break querying related objects.

        """
        author = Author.objects.create()

        book_by_author = Book.objects.create(title='book 0')
        book_no_author = Book.objects.create(title='book 1')

        author.books.add(book_by_author)

        self.assertEqual(author.books.get().title, 'book 0')
