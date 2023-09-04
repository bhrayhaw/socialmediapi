# routers for the socialmedia api
from rest_framework.routers import DefaultRouter
from follow.views import FollowViewSet, UnfollowViewSet
from post.views import PostViewSet, PostLikesViewSet, PostRepostsViewSet, PostCommentsViewSet, PostCommentRepliesViewSet
from user_registration.views import UserRegistrationView, UserLoginView
from group.views import UserGroupsViewSet

router = DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('unfollow', UnfollowViewSet, basename='unfollow')
router.register('post', PostViewSet, basename='post')
router.register('like', PostLikesViewSet, basename='like')
router.register('repost', PostRepostsViewSet, basename='repost')
router.register('comment', PostCommentsViewSet, basename='comment')
router.register('reply', PostCommentRepliesViewSet, basename='reply')
router.register('group', UserGroupsViewSet, basename='group')


urlpatterns = router.urls
