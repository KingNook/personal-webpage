from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello this is chilli\'s how can i help you today')

def scoreboard(request):
    return HttpResponse('high scores will be displayed here!')