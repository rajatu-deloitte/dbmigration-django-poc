from django.urls import path
from .views import calc

urlpatterns = [
    path('calc', calc.calculator, name='calculator'),
]