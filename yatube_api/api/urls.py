from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowAPIView, GroupViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/follow/', FollowAPIView.as_view()),
    path('v1/', include('djoser.urls.jwt')),
]
