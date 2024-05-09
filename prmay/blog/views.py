from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("HOME PAGE")

def msg(request):
    data = { 
        'title':"WARRIORS", 
        'players':['john','sam','peter','mac','johny'],
        'points':[80,60,40,50,75,45,30,20,10,85,90,76,42],
        'teams':[
            {'name':'TEAM1','city':'BHOPAL'},
            {'name':"TEAM2",'city':"DELHI"}
            ]}
    # return HttpResponse("BLOG MESSAGES!")
    return render(request, 'message.html',data)

def blog1(request):
    # return HttpResponse("BLOGs HOME PAGE")
    name = 'JOHN'
    college = "lnct"
    branch = "Computer Science"
    std_details = {'name':name,'clg':college,'branch':branch}
    return render(request,'home.html',std_details)