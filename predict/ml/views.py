from django.shortcuts import render
from django.views.generic import TemplateView
from forms import AtomForm
import predict

class IndexView(TemplateView):
    template_name = "ml/index.html"
    form_class = AtomForm

    def get_context_data(self,  **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['atomRange'] = range(0, 72)
        context['form'] = self.form_class

        return context

    def post(self, request, *args, **kwargs):
	form = self.form_class(request.POST)
        context = {}
	context['atomRange'] = range(0, 72)
        context['form'] = self.form_class

        if form.is_valid():
            predicted_data = predict.predict()
            result_y = []
            start = -10.0
            while start <= 10.0:
                result_y.append(start)
                start = start + 0.02
            final_result = []
            for i in range(len(result_y)):
                temp = []
                temp.append(result_y[i])
                temp.append(predicted_data[i])
                final_result.append(temp)
            context['result'] = final_result
        return render(request, self.template_name, context)
