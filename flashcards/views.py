# flashcards/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Deck, Card
from .serializers import DeckSerializer, DeckListSerializer, CardSerializer


class DeckViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo Deck """
    queryset = Deck.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return DeckListSerializer
        return DeckSerializer

    @action(detail=True, methods=['get'])
    def cards(self, request, pk=None):
        """Endpoint para listar todos os cards de um deck específico"""
        deck = self.get_object()
        cards = deck.cards.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


class CardViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo Card """
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = Card.objects.all()
        deck_id = self.request.query_params.get('deck', None)

        if deck_id is not None:
            queryset = queryset.filter(deck_id=deck_id)

        return queryset

    def create(self, request, *args, **kwargs):
        # Valida se o deck existe
        deck_id = request.data.get('deck')
        if not deck_id:
            return Response(
                {'error': 'O campo deck é obrigatório'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            Deck.objects.get(id=deck_id)
        except Deck.DoesNotExist:
            return Response(
                {'error': 'Deck não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )

        return super().create(request, *args, **kwargs)