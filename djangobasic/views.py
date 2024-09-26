from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello, This is home page")
    return render(request, 'index.html') 
def about(request):
    return HttpResponse("Hello, This is about page")

def contact(request):
    return HttpResponse("Hello, This is contact page")