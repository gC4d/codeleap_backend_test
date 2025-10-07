from rest_framework import serializers
from .models import Post, Like, Comment

class PostSerializer(serializers.ModelSerializer):
    # Include related likes and comments count
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content', 'likes_count', 'comments_count']
        read_only_fields = ['id', 'created_datetime', 'likes_count', 'comments_count']
        
    def __init__(self, *args, **kwargs):
        super(PostSerializer, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['username'].read_only = True
            
    def get_likes_count(self, obj):
        return obj.likes.count()
        
    def get_comments_count(self, obj):
        return obj.comments.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'username', 'created_datetime']
        read_only_fields = ['id', 'created_datetime']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'username', 'content', 'created_datetime']
        read_only_fields = ['id', 'created_datetime']