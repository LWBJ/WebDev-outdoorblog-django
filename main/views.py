from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Create your views here.
main = never_cache(TemplateView.as_view(template_name="main/build/index.html"))