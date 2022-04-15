from django.urls import path, include
from rest_framework.routers import DefaultRouter

from content.views import PostViewSet, CategoriesViewSet, CommentViewSet

router = DefaultRouter()
router.register('post', PostViewSet)
router.register('categories', CategoriesViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]