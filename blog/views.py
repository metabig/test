from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone

from blog.forms import PostForm
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView, CreateView


class postList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


class postDetail(DetailView):
    model = Post
    #context_object_name: 'post'

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


class postCreate(CreateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        print(form)
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        result = super().form_valid(form)
        return result

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})
        # return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': self.object.pk}))


class postUpdate(UpdateView):
    model = Post
    template_name_suffix = '_edit'
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})
