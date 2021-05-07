from django.db import models


class Author(models.Model):
    name = models.CharField("Nome", max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("Título", max_length=128)
    isbn = models.CharField("ISBN", max_length=64)
    author = models.ManyToManyField(Author, verbose_name="Autor(es)")
    published_by = models.CharField("Editora", max_length=128)
    book_edition = models.CharField("Edição", max_length=128)
    pages = models.IntegerField("Número de páginas")
    description = models.TextField("Descrição")

    def __str__(self):
        return self.title
