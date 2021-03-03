# pages/urls.py
from django.urls import path
from .views import SankeyView, handle_post

urlpatterns = [
    path('api/sankey/generate', handle_post, name="TEST"),
    path('', SankeyView.as_view(), name='Sankey'),
]
