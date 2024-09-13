from django.urls import path, include
from . import views




urlpatterns = [
    path("",views.NewsListCreateView.as_view()),
    path("<int:news_id>/vote/", views.NewsVote.as_view()),
    path("<int:news_id>/", views.ArticleDetailView.as_view()),
]




