from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def services(request):
    return HttpResponse('''
    <h1>Services</h2>
    <p>Services for you </p>
    <a href="/">Back Home</a>
    ''')