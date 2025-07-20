from django.shortcuts import render

from .form import LoginForm

def user_login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        pass
    
    return render(request, 'account/login.html', {'form': form})