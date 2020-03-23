from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.CharField(max_length=200, verbose_name='Titulo')
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now_add = False, verbose_name = "Fecha de actualización")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-created']
    
    def __str__(self):
        return self.title
