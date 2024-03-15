from django.urls import path
from II import views

urlpatterns = [
    path('', views.manipular_dados, name='manipular_dados'),
]
