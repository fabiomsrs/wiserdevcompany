from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Post, Category 


# Create your views here.

class IndexView(generic.ListView):
    model = Post
    paginate_by = 2
    template_name = 'core/index.html'
    context_object_name = 'post_list'
