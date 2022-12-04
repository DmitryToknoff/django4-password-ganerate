from django.shortcuts import render
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

# Create your views here.
def home(request):
    return render(request, 'password/Home.html')

def password(request):

    basic = ascii_lowercase
    thepassword = ''
    lenght = int(request.GET.get('lenght'))

    if request.GET.get('uppercase'):
        basic += ascii_uppercase

    if request.GET.get('numbers'):
        basic += digits

    if request.GET.get('special'):
        basic += punctuation

    for u in range(lenght):
        thepassword += random.choice(basic)

    return render(request, 'password/password.html', {'password': thepassword})


def infosite(request):
    return render(request, 'password/aboutsite.html')