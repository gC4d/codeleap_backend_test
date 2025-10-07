from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/posts', views.PostViewSet, basename='post')
router.register(r'api/likes', views.LikeViewSet, basename='like')
router.register(r'api/comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
