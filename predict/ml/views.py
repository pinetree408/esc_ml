from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "ml/index.html"

    def get_context_data(self,  **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['atomRange'] = range(0, 25)

        return context
