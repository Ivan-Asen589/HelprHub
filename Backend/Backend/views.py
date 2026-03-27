from posts.models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# This looks in the current folder (users) for forms.py
from users.forms import UserSignUpForm 

def index(request):
    return render(request, 'home.html', {})

def signup(request):
    return render(request, 'signup.html', {})
# def AddUser()
def receivers(request):
    return render(request, 'receivers.html', {})
def helpers(request):
    return render(request, 'helpers.html', {})
def helper_selector(request):
    posts = Post.objects.all()
    return render(request, 'helper_selector.html', {'posts': posts})
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user, backend='users.backends.EmailBackend')
            # Redirect based on 'type' field in your model
            if user.user_role == 'helper':
                return redirect('helpers')
            else:
                return redirect('receivers')
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_prompt(request):
    return #REPLACE THIS

@login_required
def logout_conf(request):
    logout(request.user)
    return render(request, 'home.html', {})

@login_required
def profile(request):
    return render(request, 'profile.html', {})

@login_required
def receivers(request):
    return render(request, 'receivers.html', {})

@login_required
def helpers(request):
    from django.utils import timezone
    today = timezone.now().date()
    volunteered_upcoming = Post.objects.filter(
        volunteer=request.user, date__gte=today
    ).order_by('date', 'start_time')
    next_request = volunteered_upcoming.first()
    upcoming_requests = volunteered_upcoming
    past_requests = Post.objects.filter(
        volunteer=request.user, date__lt=today
    ).order_by('-date', '-start_time')
    return render(request, 'helper_dashboard.html', {
        'next_request': next_request,
        'upcoming_requests': upcoming_requests,
        'past_requests': past_requests,
    })

@login_required
def helper_selector(request):
    return render(request, 'helper_selector.html', {})

def error_403(request, exception=None):
    return render(request, '403.html', status=403)

def error_404(request, exception=None):
    return render(request, '404.html', status=404)