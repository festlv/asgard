from .models import Card
from rest_framework import viewsets
from .serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be read
    """
    queryset = Card.objects.all_active()
    serializer_class = CardSerializer
