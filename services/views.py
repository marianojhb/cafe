from django.http import HttpResponse
from django.shortcuts import render
from .models import Service
from .consulta import return_data_from_database

# Create your views here.
def services(request):
    content = {
        "services" : Service.objects.all()[::-1],
    }
    return render(request, "services/services.html", content)

def consulta(request):
    return render(request, "services/consulta.html", { "columnas": return_data_from_database})
    