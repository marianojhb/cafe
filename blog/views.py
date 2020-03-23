from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blog(request):
    return HttpResponse('''
    <h1>Blog</h2>
    <p>Blog this</p>
    <a href="/">Back Home</a>
    ''')
