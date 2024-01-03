from django.urls import path
from . import views
#from .templates.services import views

urlpatterns = [
    path('', views.services, name="services"),
]
