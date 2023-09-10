from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import UsersSerializer


class UsersViewSets(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializer