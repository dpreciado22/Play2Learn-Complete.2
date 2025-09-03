from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    # this is rendered by vue-games/public/index.html --> templates/_base_vue.html
    template_name = "_base_vue.html"

class AnagramHuntView(TemplateView):
    template_name = "_base_vue.html"
