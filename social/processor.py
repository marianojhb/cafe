from .models import Link

def contexto_propio(request):
    context = {
        "prueba": "contexto global"
    }
    return context