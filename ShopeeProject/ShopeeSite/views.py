from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from .forms import LoginForm
from ShopeeSite import models
from .Data import Data

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
    ShopInfo = models.ShopInfo.objects.all()
    
    return render(request, 'index.html', locals())

def statistic(request):
    try:
        shop_id = request.POST['ShopID']
        num = request.POST['NumofProducts']
    except:
        shop_id = None
        num = None
        message = 'Please enter the Shopee shop ID and sequence of the products if you want to analyze.'
    
    if shop_id != None and num != None:
        data = Data(shop_id, num)
        products_ids = data.Run()
        data.close()
        
        product1_id = str(products_ids[0])
        product2_id = str(products_ids[1])
        product3_id = str(products_ids[2])
        
        post = models.ShopInfo.objects.create(shopid = shop_id,
                                              product1id = product1_id,
                                              product2id = product2_id, 
                                              product3id = product3_id)
        post.save()
        
        message = 'Successful statistics !! Please back to homepage to watch the result.'
        
    return render(request, 'statistic.html', locals())




















