from django.urls import path,include
from rest_framework import routers 
from .api.viewsets import ReserveViewSets


router = routers.DefaultRouter()
router.register('',ReserveViewSets,basename='reserve')

urlpatterns = [
    path('',include(router.urls)),
]