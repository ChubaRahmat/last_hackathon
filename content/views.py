from django_filters import rest_framework as filters
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Post, Category, Comment

from .serializers import PostListSerializer, \
    PostSerializer, CategorySerializer, CommentSerializer


# Create your views here.


class PostFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price',
                                      lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price',
                                    lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['category', 'price']


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['title', 'text']
    ordering_fields = ['price', 'title']
    filterset_class = PostFilter

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = PostListSerializer
        return serializer_class

    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [IsAuthenticated()]
    #     elif self.action in ['update', 'partial_update', 'destroy']:
    #         return [IsAuthor()]
    #     return []

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]
        return super(self.__class__, self).get_permissions()


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]
