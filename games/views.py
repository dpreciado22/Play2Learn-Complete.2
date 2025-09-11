# games/views.py
from django.views.generic import TemplateView

class GameBaseView(TemplateView):
    template_name = "_base_vue.html"
    game_slug = None
    page_title = None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["game_slug"] = self.game_slug
        ctx["page_title"] = self.page_title or self.game_slug.replace("-", " ").title()
        return ctx

class MathFactsView(GameBaseView):
    game_slug = "math-facts"
    page_title = "Math Facts"

class AnagramHuntView(GameBaseView):
    game_slug = "anagram-hunt"
    page_title = "Anagram Hunt"
