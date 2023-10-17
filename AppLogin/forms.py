from django import forms
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    choices = (
        ('', "Is this a seller account?"),
        ('1', 'Yes'),
        ('0','No'),
    )
    type = forms.ChoiceField(label='', choices=choices, required=True)
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={
        'placeholder':'Email Address',
    }))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Type your password'
    }))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Type your password again'
    }))
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ['user']
        labels = {
            'username':"",
            'fullname':'',
            'address_1':'',
            'city':'',
            'country':'',
            'phone':'',
            'zipcode': ''
        }
        widgets = {
            'username':forms.TextInput(attrs={
                'placeholder':'Username'
            }),
            'fullname':forms.TextInput(attrs={
                'placeholder':'Full Name'
            }),
            'address_1':forms.TextInput(attrs={
                'placeholder':'Detailed Address'
            }),
            'city':forms.TextInput(attrs={
                'placeholder':'City'
            }),
            'country':forms.TextInput(attrs={
                'placeholder':'Country'
            }),
            'phone':forms.TextInput(attrs={
                'placeholder':'Phone Number'
            }),
            'zipcode':forms.TextInput(attrs={
                'placeholder':'Zipcode'
            }),
        }
