from django.http import HttpResponse

def index(request):
    return HttpResponse("Кабинет сотрудника - MVP")
    
