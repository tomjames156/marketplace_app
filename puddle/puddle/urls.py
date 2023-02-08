from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import index, contact

urlpatterns = [
    path('', index, name="index"), # empty because it is the homepage
    path('contact/', contact, name="contact"), # contact template
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
