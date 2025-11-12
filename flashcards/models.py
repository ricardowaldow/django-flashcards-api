from django.db import models

class Deck(models.Model):
    """Modelo representando um baralho de flashcards"""
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Card(models.Model):
    """Modelo representando um flashcard"""
    deck = models.ForeignKey(
        Deck,
        related_name='cards',
        on_delete=models.CASCADE
    )
    front = models.TextField()
    back = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.front[:50]}..."
