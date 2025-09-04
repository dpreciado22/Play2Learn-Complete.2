from django.contrib import admin
from .models import GameScore, Review

@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'score', 'finished_at')
    list_filter  = ('game', 'finished_at')
    search_fields = ('user__username',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'featured', 'created_at')
    list_filter  = ('featured', 'created_at')
    search_fields = ('title', 'body', 'user__username')
