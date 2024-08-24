from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from user_app.models import profile

class RegisterForm(UserCreationForm):
       class Meta:
        model = User 
        fields = ['username','email','password1','password2']



class ProfileUpdate(forms.ModelForm):
    Date_of_Birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date"  
        })
    )

    class Meta:
        model = profile 
        fields = '__all__'

class UserUpdate(forms.ModelForm):
    model = User
#     fields = ['username','email','password1','password2']
    fields = ['first_name','last_name ','email','username']


