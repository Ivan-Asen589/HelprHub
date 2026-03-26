from django.shortcuts import render
def index(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})
# def AddUser()
def nujdaeshti(request):
    return render(request, 'nujdaeshti.html', {})
def pomagashti(request):
    return render(request, 'pomagashti.html', {})
def helper_selector(request):
    return render(request, 'helper_selector.html', {})