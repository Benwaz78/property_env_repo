from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from public_view.models import *
from public_view.forms import *
from backend.forms import *

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# EMAIL IMPORT STARTS HERE
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# EMAIL IMPORT ENDS HERE


# Create your views here.

def home(request):
     # rent = Property.objects.filter(offer_type='Rent')[:3]
     latest = Property.objects.order_by('-created')[:3]
     sale = Property.objects.filter(offer_type='Sale')[:3]
     filter_obj = FilterForm()
     args = {'sale_key':sale, 'latest':latest, 'fil':filter_obj}
     return render(request, 'public/index.html', args)

def about(request):
     team = Team.objects.order_by('-created')
     return render(request, 'public/about.html', {'team_key':team})




def detail_about(request, team_id):
     detail = Team.objects.get(id=team_id)
     return render(request, 'public/about-detail.html', {'det': detail})

def filter_form(request):
    if request.method == 'GET':
        filter_obj = FilterForm(request.GET)
        if filter_obj.is_valid():
            location = filter_obj.cleaned_data.get('location_id')
            offer_type = filter_obj.cleaned_data.get('offer_type')
            property_type = filter_obj.cleaned_data.get('property_type_id')
            filter_query = Property.objects.filter(location_id=location, offer_type=offer_type, 
                property_type_id=property_type)
            for f in filter_query:
                print(f.offer_type)
                print(f.location_id)
                print(f.property_type_id)
            return render(request, 'public/result.html', {'fil':filter_query})
    return render(request, 'public/result.html')




def agent(request):
     return render(request, 'public/agent.html')

def rent(request):
     return render(request, 'public/rent.html')

def requests(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        location = request.POST.get('location')

        print('Fullname: ', fullname, 'Email: ', email, 'Location: ', location)

        subject = 'Request Form'
        args = {
            'fullname':fullname,
            'email':email,
            'location':location
        }
        html_message = render_to_string('public/mail-template.html', args)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_FROM
        send = mail.send_mail(subject, plain_message, from_email, ['uwazie.benedict@alabiansolutions.com', ], html_message=html_message)
        if send:
            messages.success(request, 'Email sent')
        else:
            messages.error(request, 'Email not sent')

    return render(request, 'public/request.html')

def property_details(request, slug, category_id, prop_id):
    prop_det = Property.objects.get(slug=slug)
    related_prop = Property.objects.filter(property_type_id__id=category_id)

    if request.method == 'POST':
        get_prop = Property.objects.get(id=prop_id)
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        subject = 'Agent Mail'
        agent_email = get_prop.agent_id.email
        location_id = get_prop.location_id
        agent_id = get_prop.agent_id

        args = {
            'name':name,
            'phone':phone
        }

        html_message = render_to_string('public/agent-mail-template.html', args)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_FROM
        send = mail.send_mail(subject, plain_message, from_email, [agent_email, ], html_message=html_message)
        if send:
            save_data = ContactAgent(name=name, phone=phone, agent_id=agent_id, location_id=location_id)
            save_data.save()
            messages.success(request, 'Mail Sent')
        else:
            messages.error('Email not sent')
    return render(request, 'public/property-details.html', {'prop':prop_det, 'rel':related_prop})

def buy(request):
     return render(request, 'public/buy.html')



def login_view(request):
     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)

         if user is not None:
              if user.is_superuser == True:
                   login(request, user)
                   return redirect('backend:index')
              elif not(user.is_superuser):
                   login(request, user)
                   return redirect('public_view:dashboard')
         else:
               messages.error(request, 'Username and Password do not match')
     return render(request, 'public/login.html')
         


@login_required(login_url='/pages/login-page/')
def dashboard(request):
     return render(request, 'public/dashboard.html')


# @login_required(login_url='/pages/login-page/')
# def confirm_logout(request):
#  return render(request, 'public/confirm-logout.html')

def logout_view(request):
    logout(request)
    return redirect('public_view:login_view')


def add_property(request):
    if request.method == 'POST':
        add_property = PropertyForm(request.POST, request.FILES)
        if add_property.is_valid():
            user = add_property.save(commit=False)
            user.agent_id = request.user
            user.approve = False
            user.save()
            messages.success(request, 'Property added')
    else:
        add_property =  PropertyForm()
    return render(request, 'public/add-property.html', {'add':add_property})



def view_property_byagent(request):
    views = Property.objects.filter(agent_id=request.user)
    return render(request, 'public/view-list.html', {'views':views})  




def add_location(request):
    return render(request, 'public/add-location.html')






