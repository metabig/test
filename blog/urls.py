from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList.as_view(), name='post_list'),
    path('posts', views.postList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.postDetail.as_view(), name='post_detail'),
    path('post/new/', views.postCreate.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.postUpdate.as_view(), name='post_edit'),
    path('post/<pk>/remove/', views.postDelete.as_view(), name='post_delete'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('posts/author/<int:pk>', views.postListByAuthor.as_view(), name='post_by_author'),
    path('posts/category/<int:pk>', views.postListByCategory.as_view(), name='post_by_category'),
]