# lib_exercise/api_urls.py
from django.urls import path
from .views import register_user, BookListView, borrow_book, my_loans, admin_loans , login_user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),  # POST: username + password => token
    path('books/', BookListView.as_view()),
    path('books/<int:book_id>/borrow/', borrow_book),
    path('my-loans/', my_loans),
    path('admin-loans/', admin_loans),
]
