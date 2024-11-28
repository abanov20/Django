from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class QualificationsClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            qualifications = request.POST.get('qualifications').strip()
            if qualifications == 'Junior':
                request.qualifications = 'Junior-300$'
            elif qualifications == 'Middle':
                request.qualifications = 'Middle-1000$'
            elif qualifications == 'Senior':
                request.qualifications = 'Senior-2000$'
            else:
                return HttpResponseBadRequest('у вас нет квалификации')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'qualifications', 'Квалификация не определена проверьте данные еще раз')