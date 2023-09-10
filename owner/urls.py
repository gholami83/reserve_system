from django.urls import path,include
from rest_framework import routers 
from .api.viewsets import OwnerViewSets


router = routers.DefaultRouter()
router.register('',OwnerViewSets,basename='owner')

urlpatterns = [
    path('',include(router.urls)),
]