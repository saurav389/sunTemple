from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .regform import UserRegistrationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            msg = "Account created of user {username}".format(username=username)
            messages.success(request, msg)
            print(username)
            return redirect('personal')

    else:
        form = UserRegistrationForm()

    return render(request,'signup.html',{'form':form})