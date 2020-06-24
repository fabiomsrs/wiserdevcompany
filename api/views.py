from django.shortcuts import render
from rest_framework import mixins, viewsets
from .serializers import PostSerializer
from core.models import Post

# Create your views here.
class ListPosts(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer