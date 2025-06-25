from django.db import models
from django.utils import timezone

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}+{self.last_name}"

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class BookLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.reader} borrowed {self.book}"

    def is_overdue(self):
        return self.return_date < timezone.now().date()


