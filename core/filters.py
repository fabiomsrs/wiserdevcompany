from .models import Post
import django_filters


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    categories = django_filters.CharFilter(lookup_expr='name__icontains')
    class Meta:
        model = Post
        fields = ['title','categories','content']