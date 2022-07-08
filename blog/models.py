from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    category = models.ForeignKey(
        Category, default=None, blank=True, null=True, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk'], })

    def __str__(self):
        return self.title


class PostUpdate(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"At {self.update_date} by {self.author}"
