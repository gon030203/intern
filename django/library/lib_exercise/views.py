from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate    

from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, ListView, FormView
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book, BookLoan
from .serializers import BookSerializer, BookLoanSerializer, UserSerializer

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# --- API: Đăng ký người dùng ---
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


# --- API: Danh sách sách ---
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return Book.objects.filter(Q(title__icontains=query) | Q(author__first_name__icontains=query))
        return Book.objects.all()


# --- API: Mượn sách ---
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def borrow_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)

    if BookLoan.objects.filter(book=book, reader=request.user, returned=False).exists():
        return Response({'error': 'You already borrowed this book'}, status=400)

    BookLoan.objects.create(
        book=book,
        reader=request.user,
        return_date=timezone.now().date() + timezone.timedelta(days=14)
    )
    return Response({'message': 'Book borrowed successfully'})


# --- API: Lịch sử mượn của người dùng ---
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def my_loans(request):
    loans = BookLoan.objects.filter(reader=request.user)
    serializer = BookLoanSerializer(loans, many=True)
    return Response(serializer.data)


# --- API: Admin xem danh sách mượn ---
@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def admin_loans(request):
    loans = BookLoan.objects.all()
    serializer = BookLoanSerializer(loans, many=True)
    return Response(serializer.data)


# ----------------------------
# ------- Web Views ----------
# ----------------------------

# --- Giao diện xem chi tiết sách ---
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


# --- Giao diện tạo sách ---
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'price', 'tags']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


# --- Giao diện sửa sách ---
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'price', 'tags']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


# --- Giao diện xoá sách ---
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


# --- Giao diện mượn sách ---
class BorrowBookView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'borrow_book.html'
    context_object_name = 'book'

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        if BookLoan.objects.filter(book=book, reader=request.user, returned=False).exists():
            return redirect('borrowed_books')
        BookLoan.objects.create(
            book=book,
            reader=request.user,
            return_date=timezone.now().date() + timezone.timedelta(days=14)
        )
        return redirect('borrowed_books')


# --- Giao diện xem sách đã mượn ---
class BorrowedBooksView(LoginRequiredMixin, ListView):
    model = BookLoan
    template_name = 'borrowed_books.html'
    context_object_name = 'loans'

    def get_queryset(self):
        return BookLoan.objects.filter(reader=self.request.user)


# --- Giao diện tìm kiếm theo tag ---
class BookSearchByTagView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Book.objects.filter(tags__name__iexact=tag_name)


# --- Giao diện sách rẻ ---
class CheapBooksView(ListView):
    model = Book
    template_name = 'cheap_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(price__lt=100000)


# --- Giao diện đăng ký tài khoản ---
class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
