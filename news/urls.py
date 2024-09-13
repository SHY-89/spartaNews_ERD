from django.urls import path, include
from . import views




urlpatterns = [
    path("",views.NewsListCreateView.as_view()),
        
]




