
from django.contrib import admin
from django.urls import path


from prof_site.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prof_site.urls')),
]
