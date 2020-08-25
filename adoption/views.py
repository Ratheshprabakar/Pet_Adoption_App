from django.shortcuts import render
from django.http import Http404

from .models import pet

def home(request):
	pets=pet.objects.all()
	return render(request,'home.html',{'pets':pets})

def pet_details(request,pet_id):
     try:
        Pet=pet.objects.get(id=pet_id)
     except pet.DoesNotExist:
        raise Http404("Oops, Page Not found")
     return render(request,'pet_detail.html',{'Pet':Pet})



# Create your views here.
