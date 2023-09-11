from django.urls import path,include
from rest_framework import routers 
from rest_framework import renderers
from .api.viewsets import UsersViewSets,CreateAdminViewSets,CreateRoomViewSets


CreateAdminViewSets_list = CreateAdminViewSets.as_view({
    'get': 'list',
    'post': 'create',
})
CreateAdminViewSets_detail = CreateAdminViewSets.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
UsersViewSets_list = UsersViewSets.as_view({
    'get': 'list',
    'post': 'create',
})
UsersViewSets_detail = UsersViewSets.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


router = routers.DefaultRouter()
router.register('',UsersViewSets,basename='user')
router.register(r'(?P<pk1>\d+)/hotel',CreateAdminViewSets,basename='hotel')
router.register(r'(?P<pk1>\d+)/hotel/(?P<pk2>\d+)/room',CreateRoomViewSets,basename='room')

urlpatterns = [
    path('',include(router.urls)),
    # path('',UsersViewSets_list,name='user_list'),
    # path('<int:pk>/',UsersViewSets_detail,name='user_detail'),
    # path('<int:pk>/hotel/',CreateAdminViewSets_list,name='admin_list'),
    # path('<int:pk>/hotel/<int:id>/',CreateAdminViewSets_detail,name='admin_detail'),

]