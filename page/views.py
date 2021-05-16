from django.views import generic

from .models import Product

class IndexView(generic.ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

Index = IndexView.as_view()