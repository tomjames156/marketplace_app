from django.contrib import admin
from django.urls import path

from core.views import index

urlpatterns = [
    path('', index, name="index"), # empty because it is the homepage
    path('admin/', admin.site.urls),
]
