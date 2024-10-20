from logging import root
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from pydantic import RootModel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),  # Include the URLs from mainapp
    url(r'^media/(?p<path>.*)$',serve,{'document_root': settings.MEDIA-root}),
    url(r'^static/(?p<path>.*)$',serve,{'document_root': settings.STATIC-root}),
]
