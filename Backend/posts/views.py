from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def create_post(request):
    if request.method == 'POST':
        publisher = request.POST.get('publisher')
        heading = request.POST.get('heading')
        locationTown = request.POST.get('locationTown')
        locationNeighborhood = request.POST.get('locationNeighborhood')
        description = request.POST.get('description')

        post = Post.objects.create(
            publisher=publisher,
            heading=heading,
            locationTown=locationTown,
            locationNeighborhood=locationNeighborhood,
            description=description
        )
        return redirect('post-list') 

    return render(request, 'home.html')
