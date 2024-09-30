from django.shortcuts import redirect, render
from .models import *

# Create your views here.
from django.http import HttpResponse

def home(request):
    
    peoples = [
        {'name':'Anuj','age':21},
        {'name':'Piyush','age':23},
        {'name':'Mayank','age':28},
        {'name':'Aryan','age':22},
        {'name':'Kshitij','age':24}
    ]
    
    return render(request, "index.html",context={'peoples' : peoples})
# def vege(request):
#     return render(request, "receipe.html"})


    
def login(request):
    return render(request ,"login.html")
    
     


# def login(request):
#     if request.method == "POST":
#         data = request.POST
#         receipe_image = request.FILES.get('receipe_image')
#         receipe_name = data.get('receipe_name')
#         receipe_description=data.get('receipe_description')
        
#         # print( receipe_image)
#         # print( receipe_name)
#         # print( receipe_description)
        
#         Receipe.objects.create(
#             receipe_image=receipe_image,
#             receipe_name =receipe_name,
#             receipe_description=receipe_description,
#         )
        
        # return redirect('/home/templates/login.html')
        
    
    return render(request, "login.html")

def Success_page(request):
    return HttpResponse("<h1>File load successfully</h1>")
    