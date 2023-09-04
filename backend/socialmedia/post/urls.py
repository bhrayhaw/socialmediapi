# from django.urls import path
# from post.views import PostViewSet, PostLikesViewSet, PostRepostsViewSet, PostCommentsViewSet, PostCommentRepliesViewSet


# urlpatterns = [
#     path('', PostViewSet.as_view({'get': 'list'})),
#     path('<int:pk>/', PostViewSet.as_view({'get': 'retrieve'})),
#     path('postlikes/', PostLikesViewSet.as_view({'get': 'list'})),
#     path('postlikes/<int:pk>/', PostLikesViewSet.as_view({'get': 'retrieve'})),
#     path('postreposts/', PostRepostsViewSet.as_view({'get': 'list'})),
#     path('postreposts/<int:pk>/',
#          PostRepostsViewSet.as_view({'get': 'retrieve'})),
#     path('postcomments/', PostCommentsViewSet.as_view({'get': 'list'})),
#     path('postcomments/<int:pk>/',
#          PostCommentsViewSet.as_view({'get': 'retrieve'})),
#     path('postcommentreplies/',
#          PostCommentRepliesViewSet.as_view({'get': 'list'})),
#     path('postcommentreplies/<int:pk>/',
#          PostCommentRepliesViewSet.as_view({'get': 'retrieve'})),
# ]
