# # urls to follow and unfollow users
# from django.urls import path
# from .views import FollowViewSet, UnfollowViewSet

# urlpatterns = [
#     path('userfollowing/', UnfollowViewSet.as_view({'get': 'list'})),
#     path('userfollowing/<int:pk>/',
#          UnfollowViewSet.as_view({'get': 'retrieve'})),
#     path('userfollowers/', FollowViewSet.as_view({'get': 'list'})),
#     path('userfollowers/<int:pk>/',
#          FollowViewSet.as_view({'get': 'retrieve'})),
#     path('userfollowing/<int:pk>/follow',
#          UnfollowViewSet.as_view({'post': 'create'})),
#     path('userfollowing/<int:pk>/unfollow',
#          UnfollowViewSet.as_view({'delete': 'destroy'})),
#     path('userfollowers/<int:pk>/followers',
#          FollowViewSet.as_view({'post': 'create'})),
#     path('userfollowers/<int:pk>/followerslist',
#          FollowViewSet.as_view({'get': 'list'})),
#     path('userfollowers/<int:pk>/followersdetail',
#          FollowViewSet.as_view({'get': 'retrieve'})),
# ]
