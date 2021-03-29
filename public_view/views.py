from django.shortcuts import render
from django.http import HttpResponse 
from public_view.models import *

# Create your views here.

def home(request):
     return render(request, 'public/index.html')



def about(request):
     team = Team.objects.order_by('-created')
     return render(request, 'public/about.html', {'team_key':team})


def detail_about(request, team_id):
     detail = Team.objects.get(id=team_id)
     return render(request, 'public/about-detail.html', {'det':detail})



def agent(request):
     return render(request, 'public/agent.html')




def rent(request):
     return render(request, 'public/rent.html')



def request(request):
     return render(request, 'public/request.html')



def property_details(request):
     return render(request, 'public/property-details.html')





def buy(request):
     return render(request, 'public/buy.html')




def register(request):
     return render(request, 'public/register.html')




def login(request):
     return render(request, 'public/login.html')




# def add(request):
#      return HttpResponse( 6+3 )



