from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('news/', news),
    path('contacts/', contacts),
    path('documents/', documents),
    path('filials/<slug:filial_name>/', filials),

]