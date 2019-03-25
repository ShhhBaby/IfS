from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.
def home_view(request):
    return render(request, "blog/base.html", {})


def home_view2(request):
    return render(request, "blog/youtube.html", {})

def poll(request):
    k =str( Question.question_text)
    return render(request, 'blog/poll.html', {})

def news(request):
    return render(request, 'blog/news.html', {})

def gmaps(request):
    return render(request, 'blog/googlemaps.html',{})

def shop(request):
    return render(request, 'blog/shop.html', {})

def netbank(request):
    return render(request, 'blog/netbank.html', {})
def whatsapp(request):
    return render(request, 'blog/whatsapp.html', {})