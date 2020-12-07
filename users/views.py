from django.shortcuts import HttpResponse, render
from django.http import HttpResponse


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
    if request.method=='GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'username:{username} password:{password}')
        return HttpResponse('进行注册业务处理')