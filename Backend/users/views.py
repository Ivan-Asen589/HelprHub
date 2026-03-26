from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic import DetailView, UpdateView, DeleteView

User = get_user_model()

def VerifySignUp(request):
    if request.method != 'POST':
        return None
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    minLen = 8
    maxLen = 30
    cond = [False] * 7
    
    # 0: Check if username exists
    cond[0] = not User.objects.filter(username=username).exists()
    # 1: Username length
    cond[1] = len(username) <= maxLen
    # 2 & 3: Password length
    cond[2] = len(password) >= minLen
    cond[3] = len(password) <= maxLen
    # 4, 5, 6: Character checks
    cond[4] = any(char.isdigit() for char in password)
    cond[5] = any(char.isupper() for char in password)
    cond[6] = any(char.islower() for char in password)
    
    return cond

def SignUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    ver = VerifySignUp(request)
    
    if ver and all(ver):
        # Create user with hashed password
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        # Save the role (Helper or Receiver)
        user.user_role = request.POST.get('user_role') 
        user.save()
        
        login(request, user)
        return redirect('/') 
    else:
        errorsList = []
        if ver:
            if not ver[0]: errorsList.append('Username already exists!')
            if not ver[1]: errorsList.append('Username too long!')
            if not ver[2]: errorsList.append('Password too short (min 8)!')
            if not ver[4]: errorsList.append('Password needs a digit!')
            if not ver[5]: errorsList.append('Password needs uppercase!')
            if not ver[6]: errorsList.append('Password needs lowercase!')
        return render(request, 'signup.html', {'errors': errorsList})

def LogIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Note: If your custom user uses email as the username field, this works.
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
    return render(request, 'login.html')

def LogOut(request):
    logout(request)
    return redirect('login')

# Profile and Account Management Views
class UserDetailView(DetailView):
    model = User
    template_name = 'profile.html'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'profile.html'
    fields = ['username', 'phone_number', 'town', 'neighborhood']

    def get_object(self, queryset=None):
        return self.request.user
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_account.html'
    success_url = '/login/'

    def get_object(self, queryset=None):
        return self.request.user