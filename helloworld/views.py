from django.shortcuts import render, HttpResponse

def first_view_func(request):
    """第一个 View 视图处理函数"""
    return HttpResponse('<h1>hello world</h1>')