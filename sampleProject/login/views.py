from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse
from django.http import *
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Document
from django import template

register = template.Library()



def login_index(request):
	data={'msg':'','type':'no'}
	return render(request, 'login/login.html',data)

def user_login(request):
    if request.method == 'POST':
		# Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return redirect("/home")
        else:
            return render(request, 'login/login.html',{'msg':'Invalid Username and password','type':'yes'})
 
    else:
        return render(request, 'login/home.html',{'msg':'','type':'no'})

def home(request):
    if request.user.is_authenticated:
        documents = Document.objects.all()
        #print(documents)
        return render(request, 'login/home.html',{'msg':'','type':'no','documents':documents})
    else:
        data={'msg':'','type':'no'}
        return render(request,'login/login.html',data)

def logout_view(request):
    logout(request)
    return redirect('login')

def upload_doc(request):
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST' and request.FILES:
        newdoc = Document(docfile=request.FILES['docfile'])
        newdoc.save()
        return redirect("/home")
    else:
        return redirect("/home")

def delete_doc(request):
    idval = request.GET['id']
    document = Document.objects.all()
    document.delete()
    return redirect("/home")

def returnFileData(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        
        for document in documents:
            url = document.docfile.url
            name = document.docfile.name
            size = document.docfile.size/1024
            filelist = name.split('.')
            filetype =filelist[-1]
            #acctime = document.docfile.lastModified 

        value = { 
        'url': url,
        'name': name,
        'size': size,
        'filetype': filetype,
                      
        } 
        return HttpResponse(json.dumps(value), content_type="application/json")

        


