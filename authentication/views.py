from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from authentication.Forms import LoginForm


def login_user(request):
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'login_form': LoginForm(),
                    'attention': f'Wrong User: {username} or password combination!'
                           }

    return render(request, 'auth/login.html', context)

def register(request):
    return render(request, 'auth/register.html')

def logout_user(request):
    logout(request)
    return redirect('index')