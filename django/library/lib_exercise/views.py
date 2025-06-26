from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author, Tag, Reader, BookLoan

# Class-based view for book list
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'author', 'published_date', 'price', 'tags']  # Thêm 'tags'

    def get_success_url(self):
        return reverse_lazy('book_list')  # Redirect to book list after adding a book


# Class-based view for updating an existing book
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'author', 'published_date', 'price', 'tags']  # Thêm 'tags'

    def get_success_url(self):
        return reverse_lazy('book_list')  # Redirect to book list after updating a book


# Class-based view for deleting a book
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    context_object_name = 'book'

    def get_success_url(self):
        return reverse_lazy('book_list')  # Redirect to book list after deleting a book


# Class-based view for searching books by tag
class BookSearchByTagView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Book.objects.filter(tags__name=tag_name)


# Class-based view for displaying cheap books
class CheapBooksView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(price__lt=100)


# Class-based view for displaying borrowed books of a reader
class BorrowedBooksView(ListView):
    model = BookLoan
    template_name = 'library/borrowed_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        reader_id = self.kwargs['reader_id']
        return BookLoan.objects.filter(reader_id=reader_id)
