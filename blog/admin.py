from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "author", "published", "post_categories")

    # ordering para ordenar la tabla
    ordering = ("author","published")
    
    # "author__username", "categories__name" son variables globales que se crean automaticamente
    # search_fields muestra una lupa para buscar en estos campos
    search_fields = ("title", "content", "author__username", "categories__name")


    list_filter = ("author__username", "categories__name")

    # Creamos un método para publicar
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name") ])

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
