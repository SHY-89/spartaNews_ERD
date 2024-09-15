from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView
from . import views


app_name= 'accounts'
urlpatterns = [
    path("login/",  TokenObtainPairView.as_view()),
    path("signup/", views.Signup.as_view()),
    path("logout/", TokenBlacklistView.as_view()),
    path('profile/<str:username>/', views.UserProfileView.as_view()),
    path("test-email/", views.TestEmail.as_view()),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
]