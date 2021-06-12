from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('covid_by_country.urls'))
]

urlpatterns += staticfiles_urlpatterns()