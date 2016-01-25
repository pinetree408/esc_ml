from django.shortcuts import render
from django.views.generic import TemplateView
from forms import AtomForm
import predict

class IndexView(TemplateView):
    template_name = "ml/index.html"
    form_class = AtomForm

    def get_context_data(self,  **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['atomRange'] = range(0, 25)
        context['form'] = self.form_class

        return context

    def post(self, request, *args, **kwargs):
	form = self.form_class(request.POST)
        context = {}
	context['atomRange'] = range(0,25)
        context['form'] = self.form_class

	if form.is_valid():
            context['result'] = predict.predict()
        return render(request, self.template_name, context)
