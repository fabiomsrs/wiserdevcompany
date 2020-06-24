from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('home/', views.IndexView.as_view(), name='index'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='index'),
]