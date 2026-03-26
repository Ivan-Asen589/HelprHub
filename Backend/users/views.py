from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic import DetailView, UpdateView, DeleteView

User = get_user_model()
# Create your views here.

def LogIn(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
 
def LogOut(request):
    logout(request)
    return redirect('login')

class UserDetailView(DetailView):
    model = User
    template_name = 'profile.html'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'profile.html'
    fields = ['username', 'password', 'phone_number', 'town', 'neighborhood']

    def get_object(self, queryset=None):
        return self.request.user
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_account.html'
    success_url = '/login/'

    def get_object(self, queryset=None):
        return self.request.