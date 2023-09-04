from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    follow=serializers.ReadOnlyField(source='follow.username')
    unfollow=serializers.ReadOnlyField(source='unfollow.username')
    class Meta:
        model = Follow
        fields = ('id', 'owner', 'follow', 'unfollow')