from django.http import HttpResponse
from django.shortcuts import render
from .models import Services

# Create your views here.
def services(request):
    content = {
        "services" : Services.objects.all()[::-1],
    }
    return render(request, "services/services.html", content)