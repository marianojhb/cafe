from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sample(request):
    return HttpResponse('''
    <h1>Sample</h2>
    <p>Sample </p>
    <a href="/">Back Home</a>
    ''')
