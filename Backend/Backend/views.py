from django.shortcuts import render
from posts.models import Post

def index(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})
def signup(request):
    return render(request, 'signup.html', {})
# def AddUser()
def nujdaeshti(request):
    return render(request, 'nujdaeshti.html', {})
def pomagashti(request):
    return render(request, 'pomagashti.html', {})
def helper_selector(request):
    posts = Post.objects.all()
    return render(request, 'helper_selector.html', {'posts': posts})
def profile(request):
    return render(request, 'profile.html', {})
