from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404


# 게시판 목록 기능 (누구나 이용 가능)
class NewsListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        articles=Article.objects.all()
        serializer= ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author= request.user)
            return Response(serializer.data)

class NewsVote(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, news_id):
        article = get_object_or_404(Article, id=news_id)
        if request.user in article.vote.all():
            article.vote.remove(request.user)
            return Response("추천 취소")
        else:
            article.vote.add(request.user)
            return Response("추천 완료!")


class ArticleDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    # 게시글 상세 조회
    def get(self, request, news_id):
        article = get_object_or_404(Article, pk=news_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 게시글 수정
    def put(self, request, news_id):
        article = get_object_or_404(Article, pk=news_id)
        if article.author != request.user:
            return Response("권한 없음", status=400)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    # 게시글 삭제
    def delete(self, request, news_id):
        article = get_object_or_404(Article, pk=news_id)
        article.delete()
        return Response(status=204)