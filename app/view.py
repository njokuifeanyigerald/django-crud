from django.shortcuts import redirect, render, get_object_or_404
from .models import CRUD
from .forms import CRUDFORM

def home(request):
    queryset = CRUD.objects.all().order_by('-date')
    context = {
        'queryset': queryset
    }
    return render(request, 'app/base.html', context)


def create(request):
    form = CRUDFORM(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {
        "form":form
    }
    return render(request, 'app/createform.html', context)

def detail(request, detail_id):
    # print(detail_id)
    data = get_object_or_404(CRUD, pk=detail_id)
    context = {
        "data":data
    }
    return render(request, "app/detail.html", context)

def update(request, id):                                         
    # data =CRUD.objects.get(id=id) 
    # or
    data = get_object_or_404(CRUD, id=id)
    form = CRUDFORM(instance=data)                                                               

    if request.method == "POST":
        form = CRUDFORM(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {
        "form":form
    }
    return render(request, 'app/createform.html', context)


def delete(request, id):
    data = get_object_or_404(CRUD, id=id) 
    if request.method == 'POST':
        data.delete()
        return redirect('home')
    return render(request, 'app/delete.html')


