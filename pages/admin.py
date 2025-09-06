from django.contrib import admin
from .models import GameScore, Review

@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'score', 'finished_at')
    list_filter  = ('game', 'finished_at')
    search_fields = ('user__username',)
    def get_readonly_fields(self, request, obj=None):
        return ("finished_at",) if obj else ()

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'featured', 'slug', 'created_at', 'updated_at')
    list_filter  = ('featured', 'created_at')
    search_fields = ('title', 'body', 'user__username')
    def get_readonly_fields(self, request, obj=None):
        return ("slug", "created_at", "updated_at") if obj else ()