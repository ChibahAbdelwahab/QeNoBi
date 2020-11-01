from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('groups', views.GroupView)
router.register('links', views.LinkView)

urlpatterns = [
    path('', include(router.urls)),
]
