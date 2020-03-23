from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


# def index(request):
#     return HttpResponse(
#         '''
#         <h1>Home</h1>
#         <hr>
#         <ul>
#             <li><a href="#">Home</a></li>
#             <li><a href="/about">About</a></li>
#             <li><a href="/services">Servicios</a></li>
#             <li><a href="/store">Shop</a></li>
#             <li><a href="/contact">Contact us</a></li>
#             <li><a href="/blog">Blog</a></li>
#         </ul>
#         <hr>
#         <h2>Welcome to Café shop</h2>
#         <p>Your are invited to see our products in the site, but also encouraged to come up and taste our coffe at a store near you.</p>
#         '''
#     )

