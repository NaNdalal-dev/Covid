from django.urls import path, include
from .views import*

from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('',home),
]
