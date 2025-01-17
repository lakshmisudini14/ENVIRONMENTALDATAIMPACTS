from django.shortcuts import render
from .models import MyInfo


def home(request):
    names = MyInfo.objects.all()
    return render(request, 'myinfo/home.html', {'names': names})


from django.shortcuts import render