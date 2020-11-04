# pages/urls.py
from django.urls import path
from .views import SankeyView

urlpatterns = [
    path('', SankeyView.as_view(), name='Sankey'),
]
