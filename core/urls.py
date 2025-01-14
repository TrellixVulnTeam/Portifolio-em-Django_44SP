from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('quotes/', include('quotescrud.urls')),
    path('', include('machine_learn.urls')),
]