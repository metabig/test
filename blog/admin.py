from django.contrib import admin
from .models import Category, Post, PostUpdate

admin.site.register(Post)
admin.site.register(PostUpdate)
admin.site.register(Category)
