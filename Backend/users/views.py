from django.shortcuts import render
from models.py import User

# Create your views here.
"""
conditions:
SignUp:

"""
def VerifySignUp(username: str, password: str, email=None, phone_number=None):
    minLen = 8
    maxLen = 30
    cond = [False for i in range(6)]
    
    cond[0] = not any(elem.username==username for elem in User.objects.all()) #not: username already exists?
    
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

def SignUp(username_: str, password_: str, email_=None, phone_number_=None):
    User.objects.create(
        username=username_,
        password=password_,
        email=email_,
        phone_number=phone_number_
    )

        
    
        
    
