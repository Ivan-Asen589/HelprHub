from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, get_user_model, login, logout


User = get_user_model()
# Create your views here.
"""
conditions:
SignUp:

"""
def VerifySignUp(request):
    if request.method != 'POST':
        return None
    username=request.POST.get('username')
    password=request.POST.get('password')
    minLen = 8
    maxLen = 30
    cond = [False for i in range(7)]
    
    cond[0] = not any(elem.acc.username==username for elem in UserProperties.objects.all()) #not: username already exists?
    
    if len(username)<=maxLen:
        cond[1]=True #not: username too long?
    
    if len(password)>=minLen:
        cond[2]=True
    
    if len(password)<=maxLen:
        cond[3]=True
    
    cond[4] = any(char.isdigit() for char in password)
    cond[5] = any(char.isupper() for char in password)
    cond[6] = any(char.islower() for char in password)
    return cond


def SignUp(request):
    ver = VerifySignUp(request)
    if True not in ver:
        User.objects.create(
            username = request.POST.get('username'),
            email = request.POST.get('email'),
            password = request.POST.get('password')
        )
        
        login(authenticate(username=request.POST.get('username'), password=request.POST.get('password')))
        return redirect('home.html')
    else:
        errorsList = []
        if not ver[0]:
            errorsList.append('Username already exists!')
        elif not ver[1]:
            errorsList.append('Username too long (>30)!')
        if not ver[2]:
            errorsList.append('Password too short (<8)!')
        elif not ver[3]:
            errorsList.append('Password too long (>30)!')
        if not ver[4]:
            errorsList.append('Password has no digit!')
        if not ver[5]:
            errorsList.append('Password has no uppercase letter!')
        if not ver[6]:
            errorsList.append('Password has no lowercase letter!')
        return render(request, 'signup.html', {'errors': errorsList})
    

def LogIn(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(user)
        return redirect('home.html')
    else:
        return render(request, 'login.html', {'error': 'Invalid username or password.'})
 
def LogOut(request):
    logout(request.user)
    return redirect('signup.html')
        

    






        
    
        
    
