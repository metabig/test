from unicodedata import category
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from blog.filters import PostFilter

from blog.forms import PostForm
from .models import Category, Comment, Post
from .models import PostUpdate as PostUpdateModel
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView, CreateView
from django.conf import settings
from django.contrib.auth import get_user_model


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')


class PostListByAuthor(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_author = get_object_or_404(get_user_model(), pk=id)
        return Post.objects.filter(author=target_author)


class PostListByCategory(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_category = get_object_or_404(Category, pk=id)
        return Post.objects.filter(category=target_category)


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):

        context = super(PostDetail, self).get_context_data(**kwargs)
        if 'reply' in self.kwargs:
            context['reply'] = self.kwargs['reply']
        else:
            context['reply'] = -1
        context['updates'] = PostUpdateModel.objects.filter(
            post=context['post'])
        context['related_posts'] = context['post'].related_posts.all()
        context['comments'] = Comment.objects.filter(
            post=context['post'])
        return context


class PostCreate(CreateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        result = super().form_valid(form)
        update = PostUpdateModel(
            post=self.object, update_date=timezone.now(), author=self.request.user)
        update.save()
        return result

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostUpdate(UpdateView):
    model = Post
    template_name_suffix = '_edit'
    form_class = PostForm

    def form_valid(self, form):
        now = timezone.now()
        form.instance.author = self.request.user
        result = super().form_valid(form)
        update = PostUpdateModel(
            post=self.object, update_date=now, author=self.request.user)
        update.save()
        return result

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDelete(DeleteView):
    model = Post
    success_url = "/"


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def post_list(request):
    f = PostFilter(request.GET, queryset=Post.objects.filter(
        created_date__lte=timezone.now()).order_by('-created_date'))
    return render(request, 'blog/post_list.html', {'filter': f, 'posts': f.qs})

def post_comment(request, pk, comment_id):
    text = request.POST.get('text')
    post = get_object_or_404(Post, pk=pk)
    author = get_object_or_404(get_user_model(), pk=request.user.id)
    if comment_id != '-1':
        parent = get_object_or_404(Comment, pk=comment_id)
        comment = Comment(text=text, post=post, author=author, parent=parent)
        comment.save()
    else:
        comment = Comment(text=text, post=post, author=author)
        comment.save()

    return redirect('post_detail', pk=pk)
