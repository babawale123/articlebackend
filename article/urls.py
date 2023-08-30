from django.urls import path,include
from .views import AddArticle,ArticleDetail

urlpatterns = [
   path('', AddArticle.as_view()),
   path('details/<int:pk>/', ArticleDetail.as_view())
]