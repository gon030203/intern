from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, LoginView

router = DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
]
