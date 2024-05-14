from django.shortcuts import render
from .forms import registrationForm

# Create your views here.
def index(request):
    ##pass
    return render(request, "index.html")

def registration(request):
    fm=registrationForm()
    return render(request,"registration.html",{'form':fm})