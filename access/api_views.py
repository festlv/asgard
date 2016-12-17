from .models import Card, ZoneAccessLog
from rest_framework import viewsets
from .serializers import CardSerializer, ZALSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be read
    """
    queryset = Card.objects.all_active()
    serializer_class = CardSerializer


class ZALViewSet(viewsets.ModelViewSet):
    """
    ZoneAccessLogs viewset
    """
    queryset = ZoneAccessLog.objects.none()
    serializer_class = ZALSerializer
