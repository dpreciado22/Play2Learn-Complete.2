from django.db import models
from django.contrib.auth.models import User

class GameScore(models.Model):
    GAME_CHOICES = [
        ('math_facts', 'Math Facts Practice'),
        ('anagram_hunt', 'Anagram Hunt'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    game = models.CharField(max_length=20, choices=GAME_CHOICES)
    finished_at = models.DateTimeField(auto_now_add=True)
    settings = models.JSONField(default=dict)
    score = models.IntegerField()

    class Meta:
        ordering = ['-score', 'finished_at']

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    body = models.TextField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
