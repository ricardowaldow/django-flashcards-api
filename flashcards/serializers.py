# flashcards/serializers.py
from rest_framework import serializers
from .models import Deck, Card


class CardSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Card"""
    class Meta:
        model = Card
        fields = ['id', 'deck', 'front', 'back', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class DeckSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Deck, incluindo os cards relacionados"""
    cards = CardSerializer(many=True, read_only=True)
    cards_count = serializers.IntegerField(source='cards.count', read_only=True)

    class Meta:
        model = Deck
        fields = ['id', 'name', 'cards_count', 'cards', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class DeckListSerializer(serializers.ModelSerializer):
    """Serializer mais leve para listagem de decks"""
    cards_count = serializers.IntegerField(source='cards.count', read_only=True)

    class Meta:
        model = Deck
        fields = ['id', 'name', 'cards_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']