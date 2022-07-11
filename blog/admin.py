from django.contrib import admin
from .models import Category, Comment, Post, PostUpdate

admin.site.register(Post)
admin.site.register(PostUpdate)
admin.site.register(Category)
admin.site.register(Comment)
