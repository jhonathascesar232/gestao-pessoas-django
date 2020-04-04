from django.shortcuts import render, redirect
# faz as funcões de logout
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

def myLogout(request):
    logout(request)
    return redirect('home')