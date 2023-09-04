from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Comments
from .serializers import CommentSerializer
from user_profile.permissions import IsOwnerOrReadOnly
# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)   