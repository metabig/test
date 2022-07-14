from django.urls import path

from blog.models import Post
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/reply/<int:reply>',
         views.PostDetail.as_view(), name='post_detail_reply'),
    path('post/new/', views.PostCreate.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdate.as_view(), name='post_edit'),
    path('post/<pk>/remove/', views.PostDelete.as_view(), name='post_delete'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/comment/<comment_id>',
         views.post_comment, name='post_comment'),
    path('posts/author/<int:pk>',
         views.PostListByAuthor.as_view(), name='post_by_author'),
    path('posts/category/<int:pk>',
         views.PostListByCategory.as_view(), name='post_by_category'),
    path('categories',
        views.categoryList.as_view(), name='edit_categories_list'),
    path('categories/<pk>',
         views.inlineformset, name='edit_categories'),
    path('formset',
         views.formset, name='edit_posts'),    
    path('formset',
         views.formset, name='formset'),    
    path('tech',
         views.inlineformset, name='formset'),
]
