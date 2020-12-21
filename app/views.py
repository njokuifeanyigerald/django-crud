from django.shortcuts import render, redirect
from .models import CRUD


def home(request):
    queryset = CRUD.objects.all().order_by('-date')
    context = {
        'queryset': queryset
    }
    return render(request, 'base.html', context)

def create(request):
    name= request.POST.get('name')
    age= request.POST.get('age')
    level= request.POST.get('level')

    if request.method == "POST":
        queryset = CRUD(name=name, age=age, level=level)
        queryset.save()
        return redirect ('home')
    return render(request, 'create.html')

def update(request, id):
    data = CRUD.objects.get(id=id)
    name= request.POST.get('name')
    age= request.POST.get('age')
    level= request.POST.get('level')

    if request.method == "POST":
        data(name=name, age=age, level=level)
        data.save()
        return redirect ('home')
    return render(request, 'update.html')

        



