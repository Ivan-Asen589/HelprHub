from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic import DetailView, UpdateView, DeleteView

User = get_user_model()


def VerifySignUp(request):
    if request.method != 'POST':
        return None
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    cond = [False] * 7
    cond[0] = not User.objects.filter(username=username).exists()
    cond[1] = len(username) <= 30
    cond[2] = len(password) >= 8
    cond[3] = password == confirm_password
    cond[4] = any(char.isdigit() for char in password)
    cond[5] = any(char.isupper() for char in password)
    cond[6] = any(char.islower() for char in password)
    return cond


def SignUp(request):
    if request.method != 'POST':
        return render(request, 'signup.html')
    ver = VerifySignUp(request)
    user_role = request.POST.get('user_role')
    if False not in ver:
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        user.phone_number = request.POST.get('phone_number', '')
        user.type = user_role
        user.save()
        login(request, user)
        if user_role == 'helper':
            return redirect('helper_selector')
        else:
            return redirect('nujdaeshti')
    else:
        errorsList = []
        if not ver[0]:
            errorsList.append('Username already exists!')
        elif not ver[1]:
            errorsList.append('Username too long (>30)!')
        if not ver[2]:
            errorsList.append('Password too short (min 8 chars)!')
        if not ver[3]:
            errorsList.append('Passwords do not match!')
        if not ver[4]:
            errorsList.append('Password has no digit!')
        if not ver[5]:
            errorsList.append('Password has no uppercase letter!')
        if not ver[6]:
            errorsList.append('Password has no lowercase letter!')
        return render(request, 'signup.html', {'errors': errorsList})


def LogIn(request):
    if request.method == 'POST':
        user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            if user.type == 'helper':
                return redirect('helper_selector')
            else:
                return redirect('nujdaeshti')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
    return render(request, 'login.html')


def LogOut(request):
    logout(request)
    return redirect('login')


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
