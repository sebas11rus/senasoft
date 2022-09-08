from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View


# Create your views here.


class RegistroUser(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'singup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usernamea = form.cleaned_data.get('username')
            passworda = form.cleaned_data.get('password1')
            user = authenticate(username = usernamea, password=passworda)            
            login(self.request , user)        
            return redirect('registro')
            
        else:

            return render(request, 'singup.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('/')


def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid(): 
            usernamea = form.cleaned_data.get('username')
            passworda = form.cleaned_data.get('password')
            user = authenticate(username = usernamea, password=passworda)
            if user is not None:
                login(request , user)
                return redirect('index')
            else:
                return HttpResponse("User not found")
        else:
            return render(request, 'login.html', {'form':form})