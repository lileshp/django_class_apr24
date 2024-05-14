from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            na = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            data = User(name = na, email = em, password = pw)
            data.save()
            fm = StudentRegistration()
    else:
        fm=StudentRegistration()
    std = User.objects.all()
    return render(request, 'addstudent.html',{'form':fm,'stu':std})

def update_data(request,id):
    if request.method == 'POST':
        data = User.objects.get(pk =id)
        fm = StudentRegistration(request.POST, instance = data)
        if fm.is_valid():
            fm.save()
    else:
        data = User.objects.get(pk = id)
        fm = StudentRegistration(instance = data)
    return render(request, 'updatestudent.html',{'form':fm}) 

def delete_data(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')