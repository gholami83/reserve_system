from datetime import datetime
import pytz
from rest_framework.permissions import BasePermission



class IsReservePermision(BasePermission):
    def has_permission(self, request, view):
        tehran_tz = pytz.timezone('Asia/Tehran')
        current_time = datetime.now(tehran_tz)
        until_time = view.get_serializer().data.get('until_reserve')
        if until_time is not None and current_time > until_time:
            return False
        else:
            return True