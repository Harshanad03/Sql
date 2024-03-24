from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("seung")

def shop(request):
    return HttpResponse("shop VCET")

def html(request):
    return render(request,'index.html') 
def text(request):
    return render(request,'text.html',context={"text":"the context text"}) 
def para(request,name):
    return render (request,'text.html',context={"url":name})   




