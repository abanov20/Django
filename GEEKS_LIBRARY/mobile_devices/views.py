from .models import Device
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models

class DeviceListView(generic.ListView):
    template_name = 'device.html'
    context_object_name = 'device_list'
    model = models.Device

    def get_queryset(self):
        return self.model.objects.select_related().order_by('-id')

class DeviceDetailView(generic.DetailView):
    template_name = 'device_detail.html'
    context_object_name = 'device_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Device, id=book_id)

def all_models_lists_view(request):
    if request.method == 'GET':
        models_list = models.Model.objects.filter().order_by('-id')
        context = {'models_list': models_list}
        return render(request, 'all_model_list_view.html',
                      context=context)

def Apple_list_view(request):
    if request.method == 'GET':
        apple = models.Model.objects.filter(tags__name='айфон').order_by('-id')
        context = {'apple': apple}
        return render(request, 'apple.html',
                      context=context)

def xiomi_list_view(request):
    if request.method == 'GET':
        xiomi = models.Model.objects.filter(tags__name='ксяоми').order_by('-id')
        context = {'xiomi': xiomi}
        return render(request, 'xiomi.html',
                      context=context)
