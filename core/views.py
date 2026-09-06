from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Employee

def index(request):
    return HttpResponse("Кабинет сотрудника - MVP")
    
@login_required
def profile_view(request):
    """
    Страница сотрудника
    """
    employee = get_object_or_404(Employee, user=request.user)

    return render(request, "core/profile.html", {"employee":employee})

