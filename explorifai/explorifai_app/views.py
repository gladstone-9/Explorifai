from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from Constants import google_maps_key
from .models import *
import time
from django.http import JsonResponse
import json

'''
PerplexityAI
'''
from openai import OpenAI

YOUR_API_KEY = ""

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")









'''
Hugging Face Setup
'''
# Hugging Face Credientials
from dotenv import dotenv_values

secrets = dotenv_values('hf.env')
# hf_email = secrets['EMAIL']
# hf_pass = secrets['PASS']

hf_email = ''
hf_pass = ''


# LLM Response Geenration
from hugchat import hugchat
from hugchat.login import Login

def create_chatbot(email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot

def create_new_conversation(chatbot):
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)

chatbot = create_chatbot(hf_email, hf_pass)
# create_new_conversation(chatbot)

# Google API key stored locally
google_key = google_maps_key

# Create your views here.

class HomePageView(generic.base.TemplateView):
    template_name = "home.html"

def AboutPageView(request):
    return HttpResponse("Hello, world. You're at the about index.")

class WorldPageView(generic.ListView):
    Model = Location
    template_name = "explore.html"
    context_object_name = 'locations'

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_key'] = google_key
    
    # def get_historical_description(address):
    #     prompt = f"In under 100 words, what is the historical significance of the following location: {address}"             
    #     response = chatbot.chat(prompt)
    #     print(response) # Testing
    #     return response

def get_description(address):
        prompt = address            
        # response = chatbot.chat("Hello")      # Hugging Chat API wasn't working
        
        # Query PerplexityAI 
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an artificial intelligence assistant and you need to "
                    "describe the historical signifance of a location in under 100 words."
                ),
            },
            {
                "role": "user",
                "content": (
                    prompt
                ),
            },
        ]

        # chat completion without streaming
        response = client.chat.completions.create(
            model="mistral-7b-instruct",
            messages=messages,
        )

        # Testing
        # response = "test_prompt"
        # return response

        # print(response) # Testing
        return response.choices[0].message.content

def process_address(request):
    if request.method == 'POST':
        # Format request from page
        data = json.loads(request.body)
        address = str(data.get('address'))

        # Process the address data as needed
        processed_data = get_description(address)

        # # Save the data.
        # location = Location.objects.get_or_create(address=address)
        # location.description

        # Format response
        processed_data_formatted = json.dumps({'historical_description': processed_data})

        return JsonResponse({'processed_data': processed_data_formatted})
    else:
        return JsonResponse({'error': 'Invalid request method'})
