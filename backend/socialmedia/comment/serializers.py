from rest_framework import serializers
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comments
        fields = ('id', 'comment', 'comment_image','comment_video', 'comment_date', 'owner', 'post')