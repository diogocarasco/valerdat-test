# valerdat/valerdatapi/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from valerdat_api import urls as valerdat_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('valerdat/prods/', include(valerdat_urls)),
    path('valerdat/coordsprods/', include(valerdat_urls)),
    path('valerdat/shearchcoords/', include(valerdat_urls)),
]