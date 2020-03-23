from django.http import HttpResponse
from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    content = {
        "services" : Service.objects.all()[::-1],
    }
    return render(request, "services/services.html", content)