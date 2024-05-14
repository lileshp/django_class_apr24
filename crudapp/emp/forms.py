from django import forms
from .models import User
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control','id':'name','required':'Enter Name'}),
            'email':forms.EmailInput(attrs = {'class':'form-control','required':'Enter EMAIL'}),
            'password':forms.PasswordInput(attrs = {'class':'form-control','required':'Enter PAssword'}),
        }


# class StudentRegistration(forms.Form):
#     name = forms.TextInput(attrs = {'class':'form-control','id':'name'}, error_messages = {'required':'Enter Name'}),
#     email = forms.EmailInput(attrs = {'class':'form-control'},error_messages = {'required':'Enter EMAIL'}),
#     password = forms.PasswordInput(attrs = {'class':'form-control'},error_messages = {'required':'Enter PAssword'})