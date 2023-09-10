from django.urls import path,include
from rest_framework import routers 
from .api.viewsets import UsersViewSets



router = routers.DefaultRouter()
router.register('',UsersViewSets,basename='users')

urlpatterns = [
    path('',include(router.urls)),
]