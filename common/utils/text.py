import random, string
from django.utils.text import slugify

def random_string(num_chars=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(num_chars))

def unique_slug(s, model, num_chars=50, slug_field="slug"):
    base = slugify(s)[:num_chars].strip("-")
    slug = base or random_string(min(10, num_chars))  

    
    while model.objects.filter(**{slug_field: slug}).exists():
        rand = random_string(10)
        keep = max(1, num_chars - 1 - len(rand))  
        slug = f"{base[:keep]}-{rand}" if base else rand[:num_chars]
    return slug