from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("<u>Welcome to Django<u>")
def aboutpageview(request):
    return HttpResponse("<b>This is about Page</b>")
def contactpageview(request):
    return HttpResponse("This is Contact page")