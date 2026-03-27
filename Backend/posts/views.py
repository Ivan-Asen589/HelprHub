from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'nujdaeshti.html'
    fields = ['description', 'date', 'time', 'locationTown', 'locationNeighborhood']
    success_url = '/helpers/'

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(publisher=self.request.user)
        return context

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['description', 'date', 'time', 'locationTown', 'locationNeighborhood']

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.publisher != self.request.user:
            raise PermissionDenied
        return post

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = '/posts/'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.publisher_id != self.request.session.get('user_id'):
            raise PermissionDenied
        return post