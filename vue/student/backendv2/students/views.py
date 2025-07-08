from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Student
from .serializers import StudentSerializer
from .permissions import IsAdmin

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]

class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password")
        )
        if not user:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        token = RefreshToken.for_user(user)
        return Response({
            "token": str(token.access_token),
            "role": user.role
        })
