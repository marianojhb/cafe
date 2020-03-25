from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    
    # 'default=True' hace que 
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicación")
    content = models.TextField(max_length=200, verbose_name="Contenido")
    image = models.ImageField(verbose_name="Image", upload_to="blog")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_posts")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created']
    
    def __str__(self):
        return self.title
