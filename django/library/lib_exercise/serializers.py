from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Author, Book, Tag, BookLoan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

class BookLoanSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    reader = UserSerializer()

    class Meta:
        model = BookLoan
        fields = '__all__'
