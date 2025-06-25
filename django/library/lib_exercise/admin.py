from django.contrib import admin
from .models import Author, Tag, Book, Reader, BookLoan

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(BookLoan)