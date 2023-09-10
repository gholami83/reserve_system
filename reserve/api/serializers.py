from rest_framework.serializers import ModelSerializer
from ..models import Reserve


class ReserveSerializer(ModelSerializer):
    class Meta:
        model = Reserve
        fields = [
            'owner',
            'room',
            'reserved',
        ]
        