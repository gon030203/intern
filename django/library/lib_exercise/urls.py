from django.urls            import path
from .views                 import (
    BookListView, BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView, BookSearchByTagView,
    CheapBooksView, BorrowedBooksView, BorrowBookView,
    RegisterView
)
from django.contrib.auth.views import (LoginView,LogoutView,)

urlpatterns = [
    # --- Books
    path('',                            BookListView.as_view(),         name='book_list'),
    path('book/create/',                BookCreateView.as_view(),       name='book_create'),
    path('book/<int:pk>/',              BookDetailView.as_view(),       name='book_detail'),
    path('book/<int:pk>/update/',       BookUpdateView.as_view(),       name='book_update'),
    path('book/<int:pk>/delete/',       BookDeleteView.as_view(),       name='book_delete'),
    path('search/tag/<str:tag_name>/',  BookSearchByTagView.as_view(),  name='book_search_by_tag'),
    path('cheap-books/',                CheapBooksView.as_view(),       name='cheap_books'),

    # --- Borrow / Loan
    path('book/<int:pk>/borrow/',       BorrowBookView.as_view(),       name='borrow_book'),
    path('borrowed-books/',             BorrowedBooksView.as_view(),    name='borrowed_books'),

    # --- Auth
    path('accounts/login/',             LoginView.as_view(template_name='registration/login.html'),      name='login'),
    path('accounts/logout/',            LogoutView.as_view(next_page='login'),     name='logout'), 
    path('accounts/register/',          RegisterView.as_view(),         name='register'),
]
