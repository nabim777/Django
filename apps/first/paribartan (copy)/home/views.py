from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reuest):
    return HttpResponse("Welcome to Paribartan!!")

def register(request):
    return render(request, '')