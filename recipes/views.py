from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return HttpResponse("Home")

def contact(response):
    return HttpResponse("Contact")

def about(response):
    return HttpResponse("About")



