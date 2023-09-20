from django.utils.timezone import now
from rest_framework.permissions import BasePermission



class IsReservePermision(BasePermission):
    def has_object_permission(self, request, view, obj):
        current_time = now()
        until_reserve = obj.until_reserve

        if until_reserve is not None:
            return until_reserve < current_time

        return True
    