from django.urls import path,include
from rest_framework import routers 
from .api.viewsets import GuestViewSets


router = routers.DefaultRouter()
router.register('',GuestViewSets,basename='guest')

urlpatterns = [
    path('',include(router.urls)),
]