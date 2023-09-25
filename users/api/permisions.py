from datetime import datetime
from rest_framework.permissions import BasePermission



class IsReservePermision(BasePermission):
    def has_permission(self, request, view):
        current_time = datetime.now()
        until_time = view.get_serializer().data.get('until_reserve')
        if until_time is not None and current_time > until_time:
            return False
        else:
            return True
        

    # def has_object_permission(self, request, view, obj):
    #     current_time = timezone.now().time()  
    #     until_reserve = obj.until_reserve
    #     if until_reserve is not None:
    #         return until_reserve < current_time
    #     return True
    