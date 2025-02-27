from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import UserSerializer, LoginSerializer, TokenSerializer
from django.contrib.auth import authenticate

# User Registration View
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

# User Login View (Custom)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Token Refresh View (for renewing tokens)
from rest_framework_simplejwt.views import TokenRefreshView

class RefreshTokenView(TokenRefreshView):
    serializer_class = TokenSerializer



#####################

from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import TemplateView

# Function to return all API endpoints as JSON
def api_overview(request):
    api_endpoints = {
        "Authentication": {
            "Register": request.build_absolute_uri(reverse('register')),
            "Login": request.build_absolute_uri(reverse('login')),
            "Token Refresh": request.build_absolute_uri(reverse('token_refresh')),
        },
        "User Management": {
            "User Profile": "To be implemented",
        },
        "Courses": {
            "List Courses": request.build_absolute_uri(reverse('course-list')),
            "Course Details": request.build_absolute_uri(reverse('course-detail', args=[1])),
        },
        "Study Plans": {
            "List Study Plans": request.build_absolute_uri(reverse('studyplan-list')),
            "Study Plan Details": request.build_absolute_uri(reverse('studyplan-detail', args=[1])),
        },
        "Tasks": {
            "List Tasks": request.build_absolute_uri(reverse('task-list')),
            "Task Details": request.build_absolute_uri(reverse('task-detail', args=[1])),
        },
    }
    return JsonResponse(api_endpoints, safe=False)

# Optional: Display API Overview as an HTML Page
class ApiOverviewPage(TemplateView):
    template_name = "api_overview.html"
