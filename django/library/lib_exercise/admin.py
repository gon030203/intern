from django.contrib import admin
from .models import Book, Author, Tag, BookLoan

# Đăng ký các model vào admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price')  # Các trường hiển thị trong admin
    search_fields = ('title', 'author__first_name', 'author__last_name')  # Tìm kiếm theo tên sách và tác giả
    list_filter = ('author', 'tags')  # Bộ lọc theo tác giả và tags

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('get_full_name',)  # Hiển thị tên đầy đủ của tác giả

    # Thêm phương thức 'get_full_name' để hiển thị tên đầy đủ
    def get_full_name(self, obj):
        return obj.get_full_name()  # Trả về tên đầy đủ của tác giả
    get_full_name.admin_order_field = 'first_name'  # Có thể sắp xếp theo 'first_name'
    get_full_name.short_description = 'Full Name'  # Hiển thị dưới tên 'Full Name'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Các trường hiển thị trong admin

@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader', 'loan_date', 'return_date')  # Sửa 'borrow_date' thành 'loan_date'
    list_filter = ('reader', 'loan_date')  # Sửa 'borrow_date' thành 'loan_date'
