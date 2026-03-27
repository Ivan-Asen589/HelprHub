from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

User = get_user_model()

def VerifySignUp(request):
    if request.method != 'POST':
        return None
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    minLen = 8
    maxLen = 30
    cond = [False for i in range(7)]

    cond[0] = not User.objects.filter(username=username).exists()  # username not already used
    cond[1] = len(username) <= maxLen
    cond[2] = len(password) >= minLen
    cond[3] = len(password) <= maxLen
    cond[4] = password == confirm_password
    cond[5] = any(char.isdigit() for char in password)
    cond[6] = any(char.isupper() for char in password)
    cond.append(any(char.islower() for char in password))
    return cond

@csrf_protect
def SignUp(request):
    if request.user.is_authenticated:
        if request.user.user_role == 'helper':
            return redirect('helper_selector')
        return redirect('nujdaeshti')
    if request.method != 'POST':
        return render(request, 'signup.html')
    ver = VerifySignUp(request)
    if all(ver):
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        user.phone_number = request.POST.get('phone_number', '')
        user.user_role = request.POST.get('user_role', 'receiver')
        user.save()

        login(request, user, backend='users.backends.EmailBackend')
        if user.user_role == 'helper':
            return redirect('helper_selector')
        return redirect('nujdaeshti')
    else:
        errorsList = []
        if not ver[0]:
            errorsList.append('Username already exists!')
        if not ver[1]:
            errorsList.append('Username too long (>30)!')
        if not ver[2]:
            errorsList.append('Password too short (min 8 chars)!')
        if not ver[3]:
            errorsList.append('Password too long (max 30 chars)!')
        if not ver[4]:
            errorsList.append('Passwords do not match!')
        if not ver[5]:
            errorsList.append('Password has no digit!')
        if not ver[6]:
            errorsList.append('Password has no uppercase letter!')
        if len(ver) > 7 and not ver[7]:
            errorsList.append('Password has no lowercase letter!')
        return render(request, 'signup.html', {'errors': errorsList})

@csrf_protect
def LogIn(request):
    if request.user.is_authenticated:
        if request.user.user_role == 'helper':
            return redirect('helper_selector')
        return redirect('nujdaeshti')
    if request.method == 'POST':
        user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user, backend='users.backends.EmailBackend')
            if user.user_role == 'helper':
                return redirect('helper_selector')
            return redirect('nujdaeshti')
        return render(request, 'login.html', {'errors': ['Invalid email or password.']})
    return render(request, 'login.html')

def LogOut(request):
    logout(request)
    return redirect('login')

# --- PROFILE LOGIC ---

@login_required
def profile(request):
    """
    Handles displaying and updating the profile.
    This replaces the need for DetailView and UpdateView in one simple function.
    """
    user = request.user
    if request.method == 'POST':
        # Update text fields
        user.first_name = request.POST.get('first_name', user.first_name)
        user.phone_number = request.POST.get('phone_number', user.phone_number)
        user.description = request.POST.get('description', user.description)
        
        # Handle image upload
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']

        # Handle password change
        new_pw = request.POST.get('new_password')
        confirm_pw = request.POST.get('confirm_password')
        
        if new_pw:
            if new_pw == confirm_pw:
                user.set_password(new_pw)
                user.save()
                update_session_auth_hash(request, user) # Don't log them out
                messages.success(request, "Profile and password updated!")
            else:
                messages.error(request, "Passwords do not match.")
        else:
            user.save()
            messages.success(request, "Profile updated successfully!")
            
        return redirect('profile')

    return render(request, 'profile.html', {'user': user})

class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_account.html'
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user