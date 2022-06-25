from pipes import Template
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView
import random
import re

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lowercase = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    specials = list('-_!@#$%^&*()')
    numbers = list('0123456789')

    genereted_password = ''
    
    lenght = int(request.GET.get('lenght'))

    if request.GET.get('uppercase'):
        characters.extend(list(uppercase))
    if request.GET.get('specials'):
        characters.extend(list(specials))
    if request.GET.get('numbers'):
        characters.extend(list(numbers))
        
    for x in range(lenght):
        genereted_password += random.choice(characters)


    # validating that the password have at least one number, one uppercase and one special character
    if request.GET.get('numbers'):
        if bool(re.search(r'\d', genereted_password)) == False:
            genereted_password = list(genereted_password)
            genereted_password[random.choice(range(1, lenght + 1))] = random.choice(list(numbers));
            genereted_password = ''.join(genereted_password)
        elif genereted_password.isdigit() == True:
            genereted_password = list(genereted_password)
            genereted_password[random.choice(range(1, lenght + 1))] = random.choice(list(lowercase));
            genereted_password = ''.join(genereted_password)
        """              
        if request.GET.get('specials'):
            if  == False:
                genereted_password = list(genereted_password)
                genereted_password[random.choice(range(1, lenght + 1))] = random.choice(list(specials));
                genereted_password = ''.join(genereted_password)
                print(genereted_password)
        """        

    # return render(request, 'password.html', {'password': genereted_password})
    return render(request, 'home.html', {'password': genereted_password})

class error_404(TemplateView):
    template_name = 'error/404.html'

class error_505(TemplateView):
    template_name = 'error/500.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r= v(request)
            r.render()
            return r
        return view
