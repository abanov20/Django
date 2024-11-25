from django.views import generic
from . import models, forms
from django.http import HttpResponse

class LabirintListView(generic.ListView):
    template_name = 'labirint/labirint_list.html'
    context_object_name = 'labirint'
    model = models.labirint

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class LabirintFormView(generic.FormView):
    template_name = 'labirint/labirint_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('200 OK')
        else:
            return super(LabirintFormView, self).post(request, *args, **kwargs)
