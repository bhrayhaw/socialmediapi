from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from user_profile.views import ProfileViewSet
from post.views import PostViewSet
from comment.views import CommentViewSet
from Likes.views import LikeViewSet
from follow.views import FollowViewSet
from group.views import GroupViewSet 

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment') 
router.register(r'like', LikeViewSet, basename='like')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'group', GroupViewSet, basename='group')


urlpatterns = router.urls
urlpatterns += [
    path('auth/', obtain_auth_token),
]
