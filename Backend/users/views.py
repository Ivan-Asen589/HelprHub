from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

User = get_user_model()

def VerifySignUp(request):
    """
    Validates signup data and returns a list of booleans for 8 specific checks.
    """
    if request.method != 'POST':
        return None

    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    
    minLen = 8
    maxLen = 30
    
    # Initialize 8 conditions to match the error handling in SignUp
    cond = [False] * 8

    cond[0] = not User.objects.filter(username=username).exists()  # Username available
    cond[1] = len(username) <= maxLen                             # Username length
    cond[2] = len(password) >= minLen                             # Password min length
    cond[3] = len(password) <= maxLen                             # Password max length
    cond[4] = password == confirm_password                        # Passwords match
    cond[5] = any(char.isdigit() for char in password)            # Has digit
    cond[6] = any(char.isupper() for char in password)            # Has uppercase
    cond[7] = any(char.islower() for char in password)            # Has lowercase

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
        if not ver[0]: errorsList.append('Username already exists!')
        if not ver[1]: errorsList.append('Username too long (max 30 chars)!')
        if not ver[2]: errorsList.append('Password too short (min 8 chars)!')
        if not ver[3]: errorsList.append('Password too long (max 30 chars)!')
        if not ver[4]: errorsList.append('Passwords do not match!')
        if not ver[5]: errorsList.append('Password must contain at least one digit!')
        if not ver[6]: errorsList.append('Password must contain an uppercase letter!')
        if not ver[7]: errorsList.append('Password must contain a lowercase letter!')
        return render(request, 'signup.html', {'errors': errorsList, 'form_data': request.POST})

@csrf_protect
def LogIn(request):
    if request.user.is_authenticated:
        if request.user.user_role == 'helper':
            return redirect('helper_selector')
        return redirect('nujdaeshti')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user, backend='users.backends.EmailBackend')
            if user.user_role == 'helper':
                return redirect('helper_selector')
            return redirect('nujdaeshti')
        return render(request, 'login.html', {'errors': ['Invalid email or password.'], 'email': email})
    
    return render(request, 'login.html')

def LogOut(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    """
    Handles displaying and updating user personal info and password.
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
                update_session_auth_hash(request, user) # Prevents logout after password change
                messages.success(request, "Profile and password updated!")
            else:
                messages.error(request, "Passwords do not match.")
        else:
            user.save()
            messages.success(request, "Profile updated successfully!")
            
        return redirect('profile')

    return render(request, 'profile.html', {'user': user})

class UserDeleteView(DeleteView):
    """
    Handles account deletion.
    """
    model = User
    template_name = 'delete_account.html'
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user