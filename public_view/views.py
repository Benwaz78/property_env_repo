from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home(request):
     return render(request, 'public/index.html')



def about(request):
     return render(request, 'public/about.html')



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



