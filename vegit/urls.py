from django.urls import path
from . import views

urlpatterns = [
    path('vegitAjax/',views.vegitAjax,name="vegitAjax")
]