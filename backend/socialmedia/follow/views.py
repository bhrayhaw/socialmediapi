# # views to follow and unfollow users using viewsets
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from .models import UserFollowers, UserFollowing
# from .serializers import UserFollowersSerializer, UserFollowingSerializer


# class FollowViewSet(viewsets.ModelViewSet):
#     """
#     Viewset to follow users
#     """
#     queryset = UserFollowers.objects.all()
#     serializer_class = UserFollowersSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         """
#         Create a follower
#         """
#         serializer = UserFollowersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_queryset(self):
#         """
#         Get all followers
#         """
#         return self.queryset.filter(user=self.request.user)

#     def destroy(self, request, *args, **kwargs):
#         """
#         Delete a follower
#         """
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def perform_destroy(self, instance):
#         """
#         Perform destroy
#         """
#         instance.delete()


# class UnfollowViewSet(viewsets.ModelViewSet):
#     """
#     Viewset to unfollow users
#     """
#     queryset = UserFollowing.objects.all()
#     serializer_class = UserFollowingSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         """
#         Create a following
#         """
#         serializer = UserFollowingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_queryset(self):
#         """
#         Get all followings
#         """
#         return self.queryset.filter(user=self.request.user)

#     def destroy(self, request, *args, **kwargs):
#         """
#         Delete a following
#         """
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def perform_destroy(self, instance):
#         """
#         Perform destroy
#         """
#         instance.delete()
