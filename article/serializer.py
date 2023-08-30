from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta(object):
        model = Article
        fields = '__all__'