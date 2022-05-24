from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        'variable1':'I am a NAlem7',
        'variable2':'I am a Nabin Ale Magar'
    }
    return render(request, 'index.html',context)
    #return HttpResponse("Hello world!!!!!!\n This is a services pages")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about pages!!!!")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services Pages!!!!")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email= email, phone = phone , desc = desc, date = datetime.today())
        contact.save()
    return render(request,'contact.html')
    #return HttpResponse("This is a contact page")

def pubg(request):
    return render(request,'pubg.html')
    #return HttpResponse("This is a contact page")

def nature(request):
    return render(request,'nature.html')
    #return HttpResponse("This is an nature page")

def allgame(request):
    return render(request,'allgame.html')
    #return HttpResponse("This is an All games page")