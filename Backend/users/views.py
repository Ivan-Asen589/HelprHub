from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

def VerifySignUp(request):
    if request.method != 'POST':
        return None
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    minLen = 8
    maxLen = 30
    # Initialize all as False
    cond = [False] * 7
    
    # 0: Check if username exists
    cond[0] = not User.objects.filter(username=username).exists()
    # 1: Username length
    if len(username) <= maxLen: cond[1] = True
    # 2 & 3: Password length
    if len(password) >= minLen: cond[2] = True
    if len(password) <= maxLen: cond[3] = True
    # 4, 5, 6: Character checks
    cond[4] = any(char.isdigit() for char in password)
    cond[5] = any(char.isupper() for char in password)
    cond[6] = any(char.islower() for char in password)
    
    return cond

def SignUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    ver = VerifySignUp(request)
    
    # FIX: We want ALL conditions to be True to succeed
    if all(ver):
        # Use create_user so the password gets hashed (encrypted)
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        # Capture the role from the radio buttons we added
        user.user_role = request.POST.get('user_role') 
        user.save()
        
        login(request, user)
        return redirect('/') # Redirect to your homepage URL name
    else:
        errorsList = []
        if not ver[0]: errorsList.append('Username already exists!')
        if not ver[1]: errorsList.append('Username too long!')
        if not ver[2]: errorsList.append('Password too short (min 8)!')
        if not ver[4]: errorsList.append('Password needs a digit!')
        if not ver[5]: errorsList.append('Password needs uppercase!')
        if not ver[6]: errorsList.append('Password needs lowercase!')
        return render(request, 'signup.html', {'errors': errorsList})

def LogIn(request):
    if request.method == 'POST':
        email = request.POST.get('email') # Swapped to email
        password = request.POST.get('password')
        
        # Django authenticate usually looks for 'username', 
        # but if you have a custom user model, it uses that.
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