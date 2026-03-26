from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        publisher_id = request.session.get('user_id')
        if not publisher_id:
            return redirect('login')

        post = Post.objects.create(
            publisher_id=publisher_id,
            heading=request.POST.get('heading'),
            locationTown=request.POST.get('locationTown'),
            locationNeighborhood=request.POST.get('locationNeighborhood'),
            description=request.POST.get('description'),
        )
        return redirect('post-list')

    return render(request, 'home.html')

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.heading = request.POST.get('heading')
        post.locationTown = request.POST.get('locationTown')
        post.locationNeighborhood = request.POST.get('locationNeighborhood')
        post.description = request.POST.get('description')
        post.save()
        return redirect('post-list')

    return render(request, 'home.html', {'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')

    return render(request, 'home.html', {'post': post})
