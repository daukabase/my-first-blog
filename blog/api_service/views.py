from rest_framework import viewsets
from blog.api_service.serializers import PostSerializer
from blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class OrderedPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('published_date')
    serializer_class = PostSerializer


