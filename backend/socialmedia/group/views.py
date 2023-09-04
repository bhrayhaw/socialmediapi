# # views to create, manage, join and leave groups using viewsets
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from .models import UserGroups, GroupMembers
# from .serializers import UserGroupsSerializer, GroupMembersSerializer


# class UserGroupsViewSet(viewsets.ModelViewSet):
#     """
#     Viewset to create, manage, join and leave groups
#     """
#     queryset = UserGroups.objects.all()
#     serializer_class = UserGroupsSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         """
#         Create a group
#         """
#         serializer = UserGroupsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_queryset(self):
#         """
#         Get all groups
#         """
#         return self.queryset.filter(user=self.request.user)

#     def destroy(self, request, *args, **kwargs):
#         """
#         Delete a group
#         """
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def perform_destroy(self, instance):
#         """
#         Perform destroy
#         """
#         instance.delete()


# class GroupMembersViewSet(viewsets.ModelViewSet):
#     """
#     Viewset to join and leave groups
#     """
#     queryset = GroupMembers.objects.all()
#     serializer_class = GroupMembersSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         """
#         Create a group member
#         """
#         serializer = GroupMembersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(member=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_queryset(self):
#         """
#         Get all group members
#         """
#         return self.queryset.filter(member=self.request.user)

#     def destroy(self, request, *args, **kwargs):
#         """
#         Delete a group member
#         """
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def perform_destroy(self, instance):
#         """
#         Perform destroy
#         """
#         instance.delete()


