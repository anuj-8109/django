from django.shortcuts import render

# from vege.models import Receipe
from .models import *

# Create your views here.
def receipes(request):
    
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        
        # print( receipe_image)
        # print( receipe_name)
        # print( receipe_description)
        
        # Receipe.objects.create(
        #     receipe_image=receipe_image,
        #     receipe_name =receipe_name,
        #     receipe_description=receipe_description,
        # )
        print(f"Image: {receipe_image}, Name: {receipe_name}, Description: {receipe_description}")
    try:
        Receipe.objects.create(
        receipe_image=receipe_image,
        receipe_name=receipe_name,
        receipe_description=receipe_description,
    )
    
    except Exception as e:
        print(f"Error creating Receipe: {e}")
    

        
    
    return render(request ,"receipes.html")