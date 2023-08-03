from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Dispenser
from .serializers import DispenserSerializer

class DispenserViewSet(viewsets.ModelViewSet):
    queryset = Dispenser.objects.all()
    serializer_class = DispenserSerializer

    @action(detail=True, methods=['put','get','post'])
    def open_tap(self, request, pk=None):
        dispenser = self.get_object()
        if not dispenser.is_open:
            dispenser.is_open = True
            dispenser.opened_at = timezone.now()
            dispenser.save()
        return Response(self.serializer_class(dispenser).data)

    @action(detail=True, methods=['put', 'get', 'post'])
    def close_tap(self, request, pk=None):
        dispenser = self.get_object()
        if dispenser.is_open:
            time_diff = (timezone.now() - dispenser.opened_at).seconds
            dispenser.total_money += (time_diff * dispenser.flow_volume)
            dispenser.is_open = False
            dispenser.closed_at = timezone.now()
            dispenser.save()
        return Response(self.serializer_class(dispenser).data)
