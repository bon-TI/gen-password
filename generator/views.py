from ast import For
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

    result = ''
    sentence = ''
    
    lenght = int(request.GET.get('lenght'))

    if lenght <= 18:
        if request.GET.get('uppercase'):
            characters.extend(uppercase)
        if request.GET.get('specials'):
            characters.extend(specials)
        if request.GET.get('numbers'):
            characters.extend(numbers)
            
        for x in range(lenght):
            result += random.choice(characters)

        print(result)

        # validating that the password have at least one number, one uppercase and one special character
        if request.GET.get('numbers'):
            if bool(re.search(r'\d', result)) == False:
                result = list(result)
                result[random.choice(range(1, lenght))] = random.choice(list(numbers));
                result = ''.join(result)
            elif result.isdigit() == True:
                result = list(result)
                result[random.choice(range(1, lenght))] = random.choice(list(lowercase));
                result = ''.join(result)

        if request.GET.get('specials'):
            count = 0
            for char in result:
                if char not in specials:
                    count += 1

            if  count == lenght:
                result = list(result)
                result[random.choice(range(1, lenght))] = random.choice(list(specials));
                result = ''.join(result)
                print(result)
        
        sentence = "Your Password Is:"

    else:
        sentence = "Don't Cheat, Cheater"
        result = "f@$! y@#"

    
    # return render(request, 'password.html', {'password': genereted_password})
    return render(request, 'home.html', {'result': result, 'sentence': sentence})

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
