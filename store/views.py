from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def store(request):
    return HttpResponse('''
    <h1>Store</h2>
    <p>Store </p>
    <a href="/">Back Home</a>
    ''')