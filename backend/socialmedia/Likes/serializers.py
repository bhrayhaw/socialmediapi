from rest_framework import serializers
from .models import Likes

class LikeSerializer(serializers.ModelSerializer):
    like=serializers.ReadOnlyField(source='like.username')
    unlike=serializers.ReadOnlyField(source='unlike.username')
    class Meta:
        model = Likes
        fields = ('id', 'posts', 'like', 'unlike')