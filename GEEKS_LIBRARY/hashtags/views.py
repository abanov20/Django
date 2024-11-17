from django.shortcuts import render
from . import models

def all_products_lists_view(request):
    if request.method == 'GET':
        products_list = models.Product.objects.filter().order_by('-id')
        context = {'products_list': products_list}
        return render(request, 'all_products_list_view.html',
                      context=context)

def old_list_view(request):
    if request.method == 'GET':
        old = models.Product.objects.filter(tags__name='старики').order_by('-id')
        context = {'old': old}
        return render(request, 'old.html',
                      context=context)

def young_list_view(request):
    if request.method == 'GET':
        young = models.Product.objects.filter(tags__name='молодые').order_by('-id')
        context = {'young': young}
        return render(request, 'young.html',
                      context=context)

def children_list_view(request):
    if request.method == 'GET':
        children = models.Product.objects.filter(tags__name='дети').order_by('-id')
        context = {'children': children}
        return render(request, 'children.html',
                      context=context)