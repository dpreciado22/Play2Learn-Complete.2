from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "_base_vue.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["game_slug"] = "math-facts"
        ctx["page_title"] = "Math Facts"
        return ctx

class AnagramHuntView(TemplateView):
    template_name = "_base_vue.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["game_slug"] = "anagram-hunt"
        ctx["page_title"] = "Anagram Hunt"
        return ctx
