from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, serializers
from .serializers import FollowSerializer
from django.contrib.auth.models import User
from .models import Follow
from .permissions import hasFollowedOrReadOnly

# Create your views here.
class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, hasFollowedOrReadOnly]

    def perform_create(self, serializer):
        owner_instance = get_object_or_404(User,pk=self.request.data['owner'])

        if self.request.data['follow']:
            already_followed = Follow.objects.filter(owner=owner_instance, follow=self.request.user).exists()
            if already_followed:
                raise serializers.ValidationError({'message': 'You have already followed this user'})
            else:
                serializer.save(follow=self.request.user, owner=owner_instance)
        else:
            already_unfollowed = Follow.objects.filter(owner=owner_instance, unfollow=self.request.user).exists()
            if already_unfollowed:
                raise serializers.ValidationError({'message': 'You have already unfollowed this user'})
            else:
                serializer.save(unfollow =self.request.user, owner=owner_instance)