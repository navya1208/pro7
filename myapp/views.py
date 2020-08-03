from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def base(request):
  return render(request,"base.html")

def trial(request):
  return HttpResponse("<center><h1>Project is on air</h1></center>")

def home(request):
  return render(request,"myapp/home.html")

def profile(request):
  return render(request,"myapp/profile.html",{"name":"Navya!!!"})