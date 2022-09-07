from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View


# Create your views here.


class RegistroUser(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('index')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def singup(request):
    return render(request, 'singup.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

