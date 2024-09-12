from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path("login/",  TokenObtainPairView.as_view()),
    path("signup/", views.Signup.as_view()),
    path('profile/<str:username>/', views.UserProfileView.as_view()),
]
