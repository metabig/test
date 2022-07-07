import django_filters
from django.contrib.auth import get_user_model
from blog.models import Post, Category
"""
 Filtrar los post por título, autor y categoría 
"""
class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.ModelChoiceFilter(queryset=get_user_model().objects.all())
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'author', 'category']