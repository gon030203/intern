"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lib_exercise import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookListView.as_view(), name='book_list'),  # Danh sách sách
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),  # Chi tiết sách
    path('book/add/', views.BookCreateView.as_view(), name='add_book'),  # Thêm sách mới
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='update_book'),  # Sửa sách
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),  # Xóa sách
    
    # Các chức năng bổ sung
    path('books/tag/<str:tag_name>/', views.BookSearchByTagView.as_view(), name='search_books_by_tag'),  # Tìm kiếm sách theo tag
    path('books/cheap/', views.CheapBooksView.as_view(), name='cheap_books'),  # Sách giá rẻ
    path('reader/<int:reader_id>/borrowed_books/', views.BorrowedBooksView.as_view(), name='borrowed_books'),  # Sách đã mượn của người đọc
]

