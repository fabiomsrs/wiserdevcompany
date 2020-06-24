from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('posts/', views.ListPosts.as_view({'get': 'list'}), name='list_posts'),    
]