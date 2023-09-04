from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnlyPost
from .models import Posts

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyPost]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)