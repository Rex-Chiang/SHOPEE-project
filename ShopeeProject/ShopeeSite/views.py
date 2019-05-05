from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .forms import LoginForm
import datetime

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username = login_name, password = login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, "Successfully Login")
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, "The user is not found")
            else:
                messages.add_message(request, messages.WARNING, "Login Failed")
            #except:
                #messages.add_message(request, messages.WARNING, "The user is not found")
        else:
            messages.add_message(request, messages.INFO, "Please check the fields")
    else:
        login_form = LoginForm()

    return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "Successfully Logout")
    return redirect('/')

def index(request):

    return render(request, 'index.html', locals())
