from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about(request):
    context = {
        "year": 1978
    }
    return render(request, 'about/index.html', context)
# def about(request):
#     return HttpResponse('''
#     <h1>About</h2>
#     <p>You are making history</p>
#     <a href="/">Back Home</a>
#     ''')