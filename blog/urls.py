from django.urls import path

from blog.models import Post
from . import views

urlpatterns = [
    path('', views.post_list, name='post_filter'),
    path('posts',views.post_list, name='post_filter'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostCreate.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdate.as_view(), name='post_edit'),
    path('post/<pk>/remove/', views.PostDelete.as_view(), name='post_delete'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('posts/author/<int:pk>', views.PostListByAuthor.as_view(), name='post_by_author'),
    path('posts/category/<int:pk>', views.PostListByCategory.as_view(), name='post_by_category'),
]