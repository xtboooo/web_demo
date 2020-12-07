from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from users import models


def register(request):
    """注册View视图函数"""
    # html = """
    # <html>
    #     <head>
    #         <title>注册页面</title>
    #     </head>
    #     <body>
    #         <form action="/register/" method="post">
    #         username: <input type="text" name="username"><br>
    #         password: <input type="password" name="password"><br>
    #         <input type="submit" value="注册">
    #         </form>
    #     </body>
    # </html>
    # """
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.User.objects.create(username=username, password=password)
        # print(f'username:{username} password:{password}')
        return redirect('/login/')


def login(request):
    """登陆View视图函数"""
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password= request.POST.get('password')
        try:
            user = models.User.objects.get(username=username, password=password)
        except models.User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            return JsonResponse({'message':'login success'})
