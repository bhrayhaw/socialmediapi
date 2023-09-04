from rest_framework import serializers
from .models import Posts
from comment.serializers import CommentSerializer
from Likes.serializers import LikeSerializer
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Posts
        fields = ('id', 'text', 'image', 'video', 'created_at', 'comments', 'likes','owner')



