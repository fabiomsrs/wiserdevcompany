from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django_filters.views import FilterView
from .models import Post, Category 
from .filters import PostFilter


class IndexView(FilterView):
    model = Post
    filterset_class = PostFilter
    paginate_by = 10
    template_name = 'core/index.html'
    context_object_name = 'post_list'
