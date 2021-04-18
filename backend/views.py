from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 

from django.contrib.auth import  logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from backend.forms import *

def register_form(request):
  register_form = RegisterForm()
  if request.method == 'POST':
    register_form = RegisterForm(request.POST)
    if register_form.is_valid():
      register_form.save()
      messages.success(request, 'User Registered ')
  else:
    register_form = RegisterForm()
  return render(request, 'public/add-users.html', {'reg':register_form})



def add_location(request):
  location_form = LocationForm()
  if request.method == 'POST':
    location_form = LocationForm(request.POST)
    if location_form.is_valid():
      location_form.save()
      messages.success(request, 'Location Added')
  else:
    location_form = LocationForm()
  return render(request, 'backend/add-location.html', {'loc':location_form})


def add_property_type(request):
  property_type_form = PropertyTypeForm()
  if request.method == 'POST':
    property_type_form = PropertyTypeForm(request.POST)
    if property_type_form.is_valid():
      property_type_form.save()
      messages.success(request, 'Property Type Added')
  else:
    property_type_form = PropertyTypeForm()
  return render(request, 'backend/add-property-type.html', {'type':property_type_form})



def view_property_type(request):
  view_type = PropertyType.objects.all()
  return render(request, 'backend/view-property-type.html', {'type':view_type})


def edit_property_type(request, type_id):
  single_property_type = get_object_or_404(PropertyType, id=type_id)
  if request.method == 'POST':
    location_form = LocationForm(request.POST, instance=single_property_type)
    if location_form.is_valid():
      location_form.save()
      messages.success(request, 'Successfully added')
  else:
    location_form = LocationForm(instance=single_property_type)
  return render(request, 'backend/edit-property-type.html', {'edit_loc':location_form})

@login_required(login_url='/pages/login-page/')
def addlistings(request):
    if request.method == 'POST':
        add_property = PropertyForm(request.POST, request.FILES)
        if add_property.is_valid():
            user = add_property.save(commit=False)
            user.agent_id = request.user
            user.save()
            messages.success(request, 'Property added')
    else:
        add_property =  PropertyForm()
    return render(request, 'backend/add-listing.html', {'add':add_property})

@login_required(login_url='/pages/login-page/')
def edit_list(request, prop_id):
    get_prop_record = get_object_or_404(Property, id=prop_id)
    if request.method == 'POST':
        edit_property = PropertyForm(request.POST, request.FILES, instance=get_prop_record)
        if edit_property.is_valid():
            user = edit_property.save(commit=False)
            user.agent_id = request.user
            user.save()
            messages.success(request, 'Property edited')
    else:
        edit_property = PropertyForm(instance=get_prop_record)
    return render(request, 'backend/edit-listings.html', {'edit':edit_property})

@login_required(login_url='/pages/login-page/')
def view_list(request):
  views = Property.objects.all()
  return render(request, 'backend/listings.html', {'listings':views})

@login_required(login_url='/pages/login-page/')
def approve_property(request, pk):
    post = get_object_or_404(Property, pk=pk)
    post.approve_property()
    messages.success(request, 'Property approved successfully')
    return redirect('backend:view_list')

@login_required(login_url='/pages/login-page/')
def disapprove_property(request, pk):
    post = get_object_or_404(Property, pk=pk)
    post.disapprove_property()
    messages.error(request, 'Property disapproved ')
    return redirect('backend:view_list')

@login_required(login_url='/pages/login-page/')
def delete_property(request, prop_id):
    single_prop = get_object_or_404(Property, pk=prop_id)
    single_prop.delete()
    messages.success(request, 'Property Deleted ')
    return redirect('backend:view_list')



 

     






# Create your views here.
@login_required(login_url='/pages/login-page/')
def index(request):
     return render(request, 'backend/index.html')











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



