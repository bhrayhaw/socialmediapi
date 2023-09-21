from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Group, GroupMember
from .serializers import GroupSerializer, GroupMemberSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the group creator to the current user
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        group = self.get_object()
        user = request.user

        # Check if the user is already a member of the group
        if GroupMember.objects.filter(group=group, member=user).exists():
            return Response({'detail': 'You are already a member of this group.'}, status=status.HTTP_400_BAD_REQUEST)

        GroupMember.objects.create(group=group, member=user, role='member')
        return Response({'detail': 'You have joined the group successfully.'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        group = self.get_object()
        user = request.user
        try:
            member = GroupMember.objects.get(group=group, member=user)
            member.delete()
            return Response({'detail': 'You have left the group successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except GroupMember.DoesNotExist:
            return Response({'detail': 'You are not a member of this group.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def kick(self, request, pk=None, member_id=None):
        group = self.get_object()
        user = request.user

        # Check if the requester is the group creator
        if not GroupMember.objects.filter(group=group, member=user, role='creator').exists():
            return Response({'detail': 'You do not have permission to kick members.'}, status=status.HTTP_403_FORBIDDEN)

        try:
            member = GroupMember.objects.get(group=group, id=member_id)

            # Check if the member to be kicked is not the group creator
            if member.role == 'creator':
                return Response({'detail': 'You cannot kick the group creator.'}, status=status.HTTP_400_BAD_REQUEST)

            member.delete()
            return Response({'detail': 'The member has been kicked out of the group.'}, status=status.HTTP_204_NO_CONTENT)
        except GroupMember.DoesNotExist:
            return Response({'detail': 'Member not found in the group.'}, status=status.HTTP_404_NOT_FOUND)
