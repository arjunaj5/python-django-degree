from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(''' Congratulation. You have created your first application using django ! ''')

def home(request):
    return render(request, 'home.html')

