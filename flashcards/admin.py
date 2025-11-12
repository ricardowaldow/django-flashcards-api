# flashcards/admin.py
from django.contrib import admin
from .models import Deck, Card


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at', 'cards_count']
    search_fields = ['name']

    def cards_count(self, obj):
        return obj.cards.count()
    cards_count.short_description = 'Número de Cards'


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['front_preview', 'deck', 'created_at', 'updated_at']
    list_filter = ['deck', 'created_at']
    search_fields = ['front', 'back']

    def front_preview(self, obj):
        return obj.front[:50] + '...' if len(obj.front) > 50 else obj.front
    front_preview.short_description = 'Frente do Card'