from django.shortcuts import render, redirect
from django.http import HttpResponse 

from django.contrib.auth import  logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required





# Create your views here.
@login_required(login_url='/pages/login-page/')
def index(request):
     return render(request, 'backend/index.html')



def addlistings(request):
     return render(request, 'backend/add-listings.html')

def view_list(request):
     return render(request, 'backend/view-listings.html')

def edit_list(request):
     return render(request, 'backend/update-listings.html')




def add_location(request):
     return render(request, 'backend/add-location.html')

def edit_location(request):
     return render(request, 'backend/edit-location.html')

def view_location(request):
     return render(request, 'backend/view-location.html')




def user_profile(request):
     return render(request, 'backend/user-profile.html')

def edit_profile(request):
     return render(request, 'backend/edit-profile.html')

def view_profile(request):
     return render(request, 'backend/view-profile.html')


def admin_logout(request):
    logout(request)
    return redirect('public_view:login_view')



def add_property(request):
     return render(request, 'backend/add-property.html')

def edit_property(request):
     return render(request, 'backend/edit-property.html')

def view_property(request):
     return render(request, 'backend/view-property.html')




# def message(request):
#      return render(request, 'backend/message.html')





def change_password(request):
     return render(request, 'backend/change-password.html')




# def edit_profile(request):
#      return render(request, 'backend/edit-profile.html')




# def login(request):
#      return render(request, 'backend/add-listing.html')




def greet(request):
     return HttpResponse( 'hello from backend' )



