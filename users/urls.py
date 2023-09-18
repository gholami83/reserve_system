from django.urls import path,include
from rest_framework import routers 
from rest_framework import renderers
from .api.viewsets import CreateHotelViewSets,CreateRoomViewSets,ReserveRoomViewSets


router = routers.DefaultRouter()
router.register(r'hotel',CreateHotelViewSets,basename='hotel')
router.register(r'hotel/(?P<pk2>\d+)/room',CreateRoomViewSets,basename='room')
router.register(r'hotel/(?P<pk2>\d+)/room/(?P<pk3>\d+)/reserve',ReserveRoomViewSets,basename='reserve')

urlpatterns = [
    path('',include(router.urls)),
    # path('',UsersViewSets_list,name='user_list'),
    # path('<int:pk>/',UsersViewSets_detail,name='user_detail'),
    # path('<int:pk>/hotel/',CreateAdminViewSets_list,name='admin_list'),
    # path('<int:pk>/hotel/<int:id>/',CreateAdminViewSets_detail,name='admin_detail'),

]