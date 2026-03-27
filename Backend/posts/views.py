from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post


class RoleRequiredMixin(LoginRequiredMixin):
    required_role = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.required_role and request.user.user_role != self.required_role:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostListView(RoleRequiredMixin, ListView):
    required_role = 'helper'
    model = Post
    template_name = 'helper_selector.html'
    context_object_name = 'posts'

    def get_queryset(self):
        today = timezone.now().date()
        qs = Post.objects.filter(date__gte=today).order_by('date', 'start_time')
        username = self.request.GET.get('username', '').strip()
        city = self.request.GET.get('city', '').strip()
        date = self.request.GET.get('date', '').strip()
        if username:
            qs = qs.filter(publisher__username__icontains=username)
        if city:
            qs = qs.filter(locationTown__icontains=city)
        if date:
            qs = qs.filter(date=date)
        if self.request.GET.get('no_volunteer') or not self.request.GET:
            qs = qs.filter(volunteer__isnull=True)
        if self.request.GET.get('my_volunteered') and self.request.user.is_authenticated:
            qs = qs.filter(volunteer=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_username'] = self.request.GET.get('username', '')
        context['filter_city'] = self.request.GET.get('city', '')
        context['filter_date'] = self.request.GET.get('date', '')
        context['filter_no_volunteer'] = self.request.GET.get('no_volunteer', '')
        context['filter_my_volunteered'] = self.request.GET.get('my_volunteered', '')
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(RoleRequiredMixin, CreateView):
    required_role = 'receiver'
    model = Post
    template_name = 'recievers.html'
    fields = ['title', 'description', 'date', 'start_time', 'end_time', 'locationTown', 'locationNeighborhood']
    success_url = '/recievers/'

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        form.instance.publisher = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(publisher=self.request.user).order_by('date', 'start_time')
        return context

class PostUpdateView(RoleRequiredMixin, UpdateView):
    required_role = 'receiver'
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'description', 'date', 'start_time', 'end_time', 'locationTown', 'locationNeighborhood']
    success_url = '/recievers/'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.publisher != self.request.user:
            raise PermissionDenied
        return post

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = '/recievers/'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.publisher != self.request.user:
            raise PermissionDenied
        return post

@login_required
def volunteer_signup(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.volunteer is None and post.publisher != request.user:
        post.volunteer = request.user
        post.save()
    return redirect('/helper_selector/')

@login_required
def volunteer_optout(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.volunteer == request.user:
        post.volunteer = None
        post.save()
    return redirect('/helper_selector/')