from django.shortcuts import render
from django.http import HttpResponse
from home.models import Register
# Create your views here.
def index(request):
    return HttpResponse("Welcome to Paribartan!!")

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        birth_date = request.POST.get('birth_date')
        register = Register(name = name, phone = phone , address=address, email=email , password1=password1,password2=password2,birth_date=birth_date )
        register.save()
    #return render(request, '')