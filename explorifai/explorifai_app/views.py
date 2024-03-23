from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from Constants import google_maps_key
from .models import *


# Google API key stored locally
google_key = google_maps_key

# Create your views here.

class HomePageView(generic.base.TemplateView):
    template_name = "home.html"

class AboutPageView(generic.base.TemplateView):
    template_name = "about.html"

class WorldPageView(generic.ListView):
    Model = Location
    template_name = "explore.html"
    context_object_name = 'locations'

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_key'] = google_key