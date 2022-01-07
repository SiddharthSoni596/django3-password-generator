from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.
# def home(request):
#     return HttpResponse('Hello there people')

def home(request):
    # return render(request,'generator\home.html',{'pwd':'qwerty'})
    return render(request,'generator\home.html')

def password(request):
    # return render(request,'generator\home.html',{'pwd':'qwerty'})
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend([i.upper() for i in chars])
    if request.GET.get('special'):
        chars.extend(list('!@#$%&'))
    if request.GET.get('numbers'):
        chars.extend(list('01232456789'))
    length = int(request.GET.get('length',8))
    thepassword=''
    for _ in range(length):
        thepassword += choice(chars)

    return render(request,'generator\password.html',{"pwd":thepassword})

def about(request):
    # return render(request,'generator\home.html',{'pwd':'qwerty'})
    return render(request,r'generator\About.html')




