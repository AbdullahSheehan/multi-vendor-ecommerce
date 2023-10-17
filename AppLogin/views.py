from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, ProfileForm
from .models import Profile, User
from django.contrib import messages
# Create your views here.
def signupUser(req):
    form1 = SignUpForm()
    form2 = ProfileForm()
    if(req.method == 'POST'):
        form1 = SignUpForm(req.POST)
        form2 = ProfileForm(req.POST)
        if (form1.is_valid()) and (form2.is_valid()):
            user = form1.save(commit=False)
            acc_type = form1.cleaned_data.get('type')
            user.is_seller = True if acc_type == '1' else False
            user.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(req, "Account Profile Created Successfully")
            return HttpResponseRedirect(reverse('AppLogin:login'))
    return render(req, 'AppLogin/signup.html', context={'user':form1, 'profile':form2})

def loginUser(req):
    form = AuthenticationForm()
    if req.method=='POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                messages.success(req, 'You have successfully logged in!')
                return HttpResponseRedirect(reverse('AppLogin:profile'))
    return render(req, 'AppLogin/login.html', context={'form':form})
@login_required
def logoutUser(req):
    logout(req)
    messages.warning(req, "You have been logged out")
    return HttpResponseRedirect(reverse('AppLogin:login'))
@login_required
def profileUser(req):
    profile = Profile.objects.get(user=req.user)
    return render(req, 'AppLogin/profile.html', context={'profile':profile})
@login_required
def editProfile(req):
    profile = Profile.objects.get(user=req.user)
    form = ProfileForm(instance=profile)
    if req.method=='POST':
        form = ProfileForm(req.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(req, 'Successfully updated your profile')
            form = ProfileForm(instance=profile)
            return HttpResponseRedirect(reverse('AppLogin:profile'))
    return render(req, 'AppLogin/editprofile.html', context={'form':form})