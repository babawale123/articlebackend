from django.shortcuts import render
from .models import Article

from .serializer import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework import permissions, authentication


class AddArticle(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        article = Article.objects.filter(user=request.user)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    # def get(self, request):
    #     user_articles = Article.objects.filter(user=request.user)
    #     serializer = ArticleSerializer(user_articles, many=True)
    #     return Response(serializer.data)  

class ArticleDetail(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_wale(self, pk):
        try:
            return Article.objects.get(pk=pk, user=self.request.user)
        except Article.DoesNotExist:
            return None

    def get(self, request, pk):
        article = self.get_wale(pk)
        if article:
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        return Response({"error": "Article not found"}, status=404)

    def put(self, request, pk):
        article = self.get_wale(pk)
        if article:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response({"error": "Article not found"}, status=404)
    
    def delete(self, request, pk):
        article = self.get_wale(pk)
        if article:
            article.delete()
            return Response({"success": "Article deleted"})
        return Response({"error": "Article not found"}, status=404)