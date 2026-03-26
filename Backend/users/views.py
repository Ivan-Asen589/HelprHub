from django.shortcuts import redirect, render
from .models import User


def VerifySignUp(username: str, password: str, email=None, phone_number=None):
    minLen = 8
    maxLen = 30
    cond = [False for i in range(7)]
    cond[0] = not any(elem.username == username for elem in User.objects.all())  # username not already taken?

    if len(username) <= maxLen:
        cond[1] = True  # username not too long?

    if len(password) >= minLen:
        cond[2] = True

    if len(password) <= maxLen:
        cond[3] = True

    cond[4] = any(char.isdigit() for char in password)
    cond[5] = any(char.isupper() for char in password)
    cond[6] = any(char.islower() for char in password)
    return cond


def SignUp(request):
    if request.method == 'POST':
        User.objects.create(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            town=request.POST.get('town'),
            neighborhood=request.POST.get('neighborhood'),
        )
        return redirect('login')

    return render(request, 'home.html')
