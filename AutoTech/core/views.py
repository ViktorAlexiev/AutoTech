# views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def statistics(response):
    return render(response, "statistics.html", {})

def card(response):
	return render(response, "card.html", {})

def search(response):
	return render(response, "search.html", {})