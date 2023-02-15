from datetime import datetime
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {"time": 'Текущее время: ' + str(datetime.now())})
