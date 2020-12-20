from django.shortcuts import render
from django.http import HttpResponse

def HomePageview(Request):
    return HttpResponse('<h1>Hola Mundo Django</h1>')

# Create your views here.
#Post   C Create
#Get    R Read
#Update U Update
#Delete D Delete