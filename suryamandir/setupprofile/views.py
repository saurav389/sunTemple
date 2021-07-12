from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from .models import PersonalDetails, QualificationDetails, LocationDetails, ProfileDetails
from .profilesetupform import (PersonalSetupForm,
                               QualificationSetupForm,
                               LocationSetupForm,
                               ProfileSetupForm
                                )
# Create your views here.


@login_required
def Personal_view(request):
    #form = PersonalSetupForm()
    #ids = request.user.id
    #user = User.objects.get(pk=ids)

    if request.method == 'POST':
        print(request.POST)
        form = PersonalSetupForm(request.POST)
        if form.is_valid():
            personalobj = form.save(commit=False)
            personalobj.user = request.user
            profile_form = ProfileSetupForm()
            profileobj = profile_form.save(commit=False)
            profileobj.user = request.user
            profileobj.MobileNo = 9791000000
            profileobj.save()
            personalobj.save()
            return redirect('/setup/qualification')
    else:
        print("get")
        form = PersonalSetupForm()
        context = {"form":form}
        return render(request,"personal.html",context)


@login_required
def Qualification_view(request):

    if request.method == 'POST':
        form = QualificationSetupForm(request.POST)
        if form.is_valid():
            qualificationobj=form.save(commit=False)
            qualificationobj.user=request.user
            qualificationobj.save()
            form = QualificationSetupForm()
            username = request.user.username
            msg = "Qualification Details for {username} saved Successfully !".format(username=request.user)
            messages.success(request,msg)
            return redirect('/setup/location')
        else:
            msg = "Form Not Valid"
            messages.alert(request,msg)
            return redirect('/setup/qualification')
    else:
        form=QualificationSetupForm()
        context = {"form":form}
        return render(request,"qualification.html",context)


@login_required
def Location_view(request):

    if request.method == 'POST':
        form = LocationSetupForm(request.POST)
        if form.is_valid():
            locationobj = form.save(commit=False)
            locationobj.user = request.user
            locationobj.save()
            form=LocationSetupForm()
            username = request.user.username
            msg = "Location Details for {username} saved Successfully !".format(username=request.user)
            return redirect('/setup/setimage')
        else:
            msg = "Form is not Valid ! Please fill CareFully"
            messages.alert(request,msg)
            return redirect('/setup/location')
    else:
        form = LocationSetupForm()
        context = {"form":form}
        return render(request,"location.html",context)

@login_required
def Profile_view(request, *args, **kwargs):
    ids = request.user.id
    user = User.objects.get(pk=ids)
    if request.method == 'POST':
        p_form = ProfileSetupForm(request.POST,request.FILES,instance=request.user.Profile)
        print("post")
        if p_form.is_valid():
            p_form.save()
            messages.success(request,'Successfully Updated')
            return redirect('profile')
        else:
            print('not valid form')
    else:
        p_form = ProfileSetupForm(instance=request.user.Profile)
        print("get")
    context = {"form":p_form}
    return render(request,"profilesetup.html",context)

def ProfileView(request):
    qr = BlogPost.objects.filter(user=request.user).count()
    blog = BlogPost.objects.filter(user=request.user)
    total = 0
    for content in blog:
        total=total + content.views

    context = {"Tblog":qr,
               "TotalViews":total
               }
    return render(request,"profile.html",context)
def PerUpdate(request):

    if request.method == 'POST':
        print(request.POST)
        form = PersonalSetupForm(request.POST,instance=request.user.PersonalDetails)
        if form.is_valid():
            personalobj = form.save(commit=False)
            personalobj.user = request.user
            personalobj.save()
            return redirect('/setup/profile')
        else:
            print("not valid")
    else:
        print("get")
        form = PersonalSetupForm(instance=request.user.PersonalDetails)
        context = {"form":form}
        return render(request,"perupdate.html",context)


def QualUpdate(request):

    if request.method == 'POST':
        print(request.POST)
        form = QualificationSetupForm(request.POST,instance=request.user.QualificationDetails)
        if form.is_valid():
            qualificationobj = form.save(commit=False)
            qualificationobj.user = request.user
            qualificationobj.save()
            return redirect('/setup/profile')
        else:
            print("not valid")
    else:
        print("get")
        form = QualificationSetupForm(instance=request.user.QualificationDetails)
        context = {"form":form}
        return render(request,"qualupdate.html",context)


def LocUpdate(request):

    if request.method == 'POST':
        print(request.POST)
        form = LocationSetupForm(request.POST,instance=request.user.LocationDetails)
        if form.is_valid():
            Locationobj = form.save(commit=False)
            Locationobj.user = request.user
            Locationobj.save()
            return redirect('/setup/profile')
        else:
            print("not valid")
    else:
        print("get")
        form = LocationSetupForm(instance=request.user.LocationDetails)
        context = {"form":form}
        return render(request,"locupdate.html",context)