from django.db import models
from logicaldelete.models import Model as LogicalDeleteModel


class Book(LogicalDeleteModel):
    title = models.TextField('title')


class Author(models.Model):
    name = models.TextField('name')
    books = models.ManyToManyField(Book)
