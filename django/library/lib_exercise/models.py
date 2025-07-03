from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return self.__str__()

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title          = models.CharField(max_length=100)
    author         = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price          = models.DecimalField(max_digits=8, decimal_places=2)
    tags           = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

class BookLoan(models.Model):
    book        = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader      = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date   = models.DateField()
    return_date = models.DateField()
    returned    = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reader.username} → {self.book.title}"

    def is_overdue(self):
        return self.return_date < timezone.now().date()

    def get_book_title(self):
        return self.book.title
