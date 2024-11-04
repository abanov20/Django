from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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