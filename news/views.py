from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


# 게시판 목록 기능 (누구나 이용 가능)
class NewsListCreateView(APIView):

    def get(self,request):
        articles=Article.objects.all()
        serializer= ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    