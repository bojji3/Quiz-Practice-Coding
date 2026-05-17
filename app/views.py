from django.shortcuts import render 
from .models import Member 
 
def index(request): 
    obj = Member.objects.all() 
    return render(request, "index.html", {"obj": obj}) 
