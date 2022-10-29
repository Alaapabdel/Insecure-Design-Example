from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.db import connection
from .models import User
import js2py

# Create your views here.
def index(request):
    if request.method == 'POST':
        del request.session['username']
        return render(request, 'index.html', {"username" : ""})
    else:
        if request.session.has_key('username'):
            username = request.session['username']
            return render(request,  'index.html', {"username" : username})
        else:
            return render(request, 'index.html', {"username" : ""})

def details(request):
    return render(request,  'details.html')

def login(request):
    args = {}
    if request.method == 'POST':
        condition = False
        try:
                myuserID = User.objects.filter(userID=request.POST.get("userID"))[0].userID                
                try:
                    int(request.POST.get("userID"))
                    condition = True
                except ValueError:
                    condition = False
                if condition == False:
                    args = {}
                    args['message'] = "Enter a number!"
                    return render(request, 'login.html',args)
        except:
            args = {}
            args['message'] = "Wrong ID!"
            return render(request, 'login.html',args)
        if myuserID == request.POST.get("userID"):
            user = User.objects.filter(userID=request.POST.get("userID"))[0]
            userID= user.userID
            name= user.name
            cc= user.cc
            pin= user.pin
            return render(request,  'details.html', {"userID" : userID, "name": name, "cc" : cc, "pin" : pin})
    else:
        return render(request, 'login.html')

def search(request):
    if request.method == 'POST':
        if request.POST.get("usersearch") is not None:
            cursor = connection.cursor()
            query = "SELECT city, street FROM lab4_branch WHERE country = '" + str(request.POST.get("usersearch")) +"'"
            branches = cursor.execute(query)
            return render(request, 'search.html', {"branches" : branches , "searched": request.POST.get("usersearch")})
    return render(request, 'search.html', {"searched": ""})
