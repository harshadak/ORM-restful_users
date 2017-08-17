from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import gmtime, strftime, localtime
from django.contrib import messages
from models import * # Need this in order to run queries


def index(request):
    context = {
        "users_all" : User.objects.all()
    }
    return render(request, 'users/users.html', context)

def new(request):
    return render(request, 'users/new.html')

def edit(request, id):
    context = {
        "user" : User.objects.get(id = id)
    }
    return render(request, 'users/edit.html', context)

def show(request, id):
    if request.method == "POST":
        return redirect('/update') # Add ID

    context = {
        "user" : User.objects.get(id = id)
    }
    return render(request, 'users/show.html', context)

def create(request):
    if request.method == "POST":
        User.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], email = request.POST["email"])
        return redirect('/users')

def destroy(request, id):
    delete_user = User.objects.get(id = id)
    delete_user.delete()
    return redirect('/users')

def update(request, id):
    update_user = User.objects.get(id = id)
    update_user.first_name = request.POST["fname"]
    update_user.last_name = request.POST["lname"]
    update_user.email = request.POST["email"]
    update_user.save()
    return redirect('/users/'+id) # Add ID