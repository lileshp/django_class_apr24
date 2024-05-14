from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"CONGRATULATIONs!")
            form.save()
    else:
        form=SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    pass

def user_logout(request):
    pass

def dashboard(request):
    pass

def add_blog(request):
    pass

def update_blog(request,id):
    pass

def delete_blog(request,id):
    pass

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')