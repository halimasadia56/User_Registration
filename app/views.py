from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def registration(request):
    ufd=UserForm()
    pfd=ProfileForm()
    d={'ufd':ufd, 'pfd':pfd}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        

        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            NSUO.set_password(ufd.cleaned_data['password'])
            NSUO.save()
    
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            return HttpResponse('data is collected sucessfully')
        
        else:
            return HttpResponse('invalid data')

    return render(request,'registration.html',d)