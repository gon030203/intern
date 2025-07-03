from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lib_exercise.urls')),  # <--- quan trọng
    path('api/', include('lib_exercise.api_urls')),  # nếu bạn có api riêng
]
