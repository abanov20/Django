from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views import generic
from . import models


#search button
class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return models.Library.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



#film list
class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = models.Library

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

#detail list
class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Library, id=book_id)
# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Library, id=id)
#         context = {'book_id': book_id}
#         return render(request, template_name='book_detail.html', context=context)

