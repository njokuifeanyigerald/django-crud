from django.shortcuts import redirect, render, get_object_or_404
from .models import CRUD
from .forms import CRUDFORM

def home(request):
    queryset = CRUD.objects.all().order_by('-date')
    context = {
        'queryset': queryset
    }
    return render(request, 'base.html', context)

def create(request):
    form = CRUDFORM(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {
        "form":form
    }
    return render(request, 'createform.html', context)

def update(request, pk):
    data = CRUD.objects.get(id=pk)
    

    if request.method == "POST":
        data(name=name, age=age, level=level)
        data.save()
        return redirect ('home')
    return render(request, 'update.html')

        


