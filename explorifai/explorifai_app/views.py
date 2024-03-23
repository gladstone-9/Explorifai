from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.

class HomePageView(generic.base.TemplateView):
    template_name = "home.html"

def AboutPageView(request):
    return HttpResponse("Hello, world. You're at the about index.")

def WorldPageView(request):
    return HttpResponse("Hello, world. You're at the world index.")