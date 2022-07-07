from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
