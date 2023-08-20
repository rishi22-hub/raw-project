from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'base.html',{})
@login_required(login_url="/admin/login")
def about(request):
    return render(request,'index.html',{})
@login_required(login_url="/admin/login")
def contact(request):
    return render(request,'index2.html',{})

def table(request):
    return HttpResponse("in Tracker")

def search(request):
    return HttpResponse("in search")

def checkout(request):
    return HttpResponse("in checkout")

def productview(request):
    return HttpResponse("in productview")