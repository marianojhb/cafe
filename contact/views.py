from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contact(request):
    return HttpResponse('''
    <h1>Contact</h2>
    <p>Contact me!</p>
    <a href="/">Back Home</a>
    ''')