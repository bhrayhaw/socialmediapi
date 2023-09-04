from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, serializers
from .serializers import LikeSerializer
from post.models import Posts
from .models import Likes
from .permissions import hasLikedOrReadOnly

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, hasLikedOrReadOnly]

    def perform_create(self, serializer):
        post_instance = get_object_or_404(Posts,pk=self.request.data['posts'])

        if self.request.data['like']:
            already_liked = Likes.objects.filter(posts=post_instance, like=self.request.user).exists()
            if already_liked:
                raise serializers.ValidationError({'message': 'You have already liked this post'})
            else:
                serializer.save(like=self.request.user, posts=post_instance)
        else:
            already_unliked = Likes.objects.filter(posts=post_instance, unlike=self.request.user).exists()
            if already_unliked:
                raise serializers.ValidationError({'message': 'You have already unliked this post'})
            else:
                serializer.save(unlike =self.request.user, posts=post_instance)