import random
from django import template
from pages.models import Review

register = template.Library()

@register.inclusion_tag('common/review_card.html')
def random_review():
    count = Review.objects.count()
    if count:
        review = Review.objects.all()[random.randrange(count)]
        return {'review': review}
    return {'review': None}