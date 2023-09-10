from django.urls import path,include
from rest_framework import routers 
from .api.viewsets import RoomViewSets,RoomChoiceViewSets,ReserveRoomViewSets


router = routers.DefaultRouter()
router.register('list',RoomViewSets,basename='room')
router.register('choice',RoomChoiceViewSets,basename='create_room')
router.register('reserve',ReserveRoomViewSets,basename='reserve_room')


urlpatterns = [
    path('',include(router.urls)),
]