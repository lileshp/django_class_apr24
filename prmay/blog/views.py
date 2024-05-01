from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("HOME PAGE")

def msg(request):
    return HttpResponse("BLOG MESSAGES!")

def blog1(request):
    # return HttpResponse("BLOGs HOME PAGE")
    return render(request,'home.html')