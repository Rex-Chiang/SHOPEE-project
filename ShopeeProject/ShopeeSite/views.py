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

def statistic(request):
    try:
        account = request.POST['account']
    except:
        account = None
        message = '如需查詢，請輸入欲查詢蝦皮店家ID'
    
    if account != None:
        url = "https://www.instagram.com/"+account+"/"
        crawler1 = Crawler1(url)
        crawler2 = Crawler2(url)

        followers, following, article = crawler2.RE(crawler2.page.find_all("script")[4].text)

        account = account.replace(".","_")

        if int(article) <= 12:
            Most_Liked_Posts, Most_Commented_Posts, Least_Liked_Posts, Least_Commented_Posts = crawler1.Run(account)
        
        else:
            Most_Liked_Posts, Most_Commented_Posts, Least_Liked_Posts, Least_Commented_Posts = crawler2.Run(account)
        
        
        post = models.Article.objects.create(account=account, followers=followers, 
                                             following=following, articles=article, 
                                             Most_Liked_Posts=Most_Liked_Posts, Most_Commented_Posts=Most_Commented_Posts,
                                             Least_Liked_Posts=Least_Liked_Posts, Least_Commented_Posts=Least_Commented_Posts)
        post.save()
        message = '統計成功 !! 請至主畫面觀看結果'
    return render(request, 'statistic.html', locals())
