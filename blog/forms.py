from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title', 'text', 'category',
                  'related_posts')

class PostFormPublished(forms.ModelForm):
    published = forms.BooleanField()

    class Meta():
        model = Post
        fields = ('title', 'text', 'category',
                  'related_posts', 'published')
