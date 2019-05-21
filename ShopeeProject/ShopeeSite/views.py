from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from .forms import LoginForm
from ShopeeSite import models
from .Data import Data

# 登入程序
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
        else:
            messages.add_message(request, messages.INFO, "Please check the fields")
    else:
        login_form = LoginForm()

    return render(request, 'login.html', locals())

# 登出程序
def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "Successfully Logout")
    return redirect('/')

# 主頁可以擷取Django資料庫的資料並顯示
def index(request):
    ShopInfo = models.ShopInfo.objects.all()
    
    return render(request, 'index.html', locals())

# 統計頁面負責呼叫Data.py及Figure.py擷取商品資訊
def statistic(request):
    try:
        shop_id = request.POST['ShopID']
        num = request.POST['NumofProducts']
    except:
        shop_id = None
        num = None
        message = 'Please enter the Shopee shop ID and sequence of the products if you want to analyze.'
    
    if shop_id != None and num != None:
        # 呼叫完整商品統計流程
        data = Data(shop_id, num)
        products_ids = data.Run()
        data.close()
        
        product_id = str(products_ids[int(num)-1])
        # 將擷取的賣場ID、商品ID存於Django資料庫
        post = models.ShopInfo.objects.create(shopid = shop_id,
                                              product_id = product_id)
        post.save()
        
        message = 'Successful statistics !! Please back to homepage to watch the result.'
        
    return render(request, 'statistic.html', locals())




















