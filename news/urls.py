from django.urls import path, include
from . import views




urlpatterns = [
    path("",views.NewsListCreateView.as_view()),
    path("<int:news_id>/vote/", views.NewsVote.as_view()),
    path("<int:news_id>/", views.ArticleDetailView.as_view()),
    path("<int:news_id>/favorite/", views.NewsFavorite.as_view()),
    path("<int:news_id>/comment/", views.CommentViewSet.as_view()),
    path("<int:news_id>/comment/<int:comment_id>/", views.CommentDeleteViewSet.as_view()),
    path("comment/<int:comment_id>/vote/", views.CommentVote.as_view()),
    path("comment/<int:comment_id>/favorite/", views.CommentFavorite.as_view()),

    path("<int:news_id>/comments/", views.CommentViewSet.as_view()),
]




