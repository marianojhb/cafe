from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView # to set favico
from django.conf.urls import url # to set favico


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('page/', include('pages.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/favicon.ico')), # to set favico
]


# aca mapeamos archivos estaticos si estamos debuggueando

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Extendemos la cfg del panel de admin

admin.site.site_header = "Cafe Cafe"
admin.site.index_title = "Panel de Administrador"
admin.site.site_title = "Cafe"