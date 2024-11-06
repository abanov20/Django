from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

#film list
def books_list_view(request):
    if request.method == 'GET':
        book_list = models.Library.objects.filter().order_by('-id')
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)

#detail list
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Library, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)

# Create your views here.
def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Ариет.Мне 14 лет, я учусь в лицее.Хочу стать backend разработчиком')

def about_my_pets(request):
    if request.method == 'GET':
        pet_name = 'Марсик'
        url_picture = '<img src = "https://www.purelypetsinsurance.co.uk/media/vxzdtmlz/scottish-fold-2.jpg?format=webp">'
        pet_url = f'имя:{pet_name}, фото:{url_picture}'
        return HttpResponse(pet_url)

def system_time(request):
    if request.method == 'GET':
        now=datetime.now()
        time_now = now.strftime("%I:%M:%S %p")
        date_now = now.strftime("%B %d, %Y")
        time_date = f'Дата:{date_now} Время:{time_now}'
        return HttpResponse(time_date)