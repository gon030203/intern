from rest_framework import serializers
from .models import Author, Tag, Book, Reader, BookLoan

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'price', 'tags']

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['id', 'name', 'email']

class BookLoanSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    reader = ReaderSerializer()

    class Meta:
        model = BookLoan
        fields = ['id', 'book', 'reader', 'loan_date', 'return_date']