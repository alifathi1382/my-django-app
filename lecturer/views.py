from django.shortcuts import render, redirect
from .forms import LecturerForm
from .models import Lecturer


# Create your views here.
def lecturerformview(request):
    form = LecturerForm
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecshow_url')
    context = {'form': form}
    return render(request, 'lecturer.html', context)


def lecshowview(request):
    obj = Lecturer.objects.all()
    context = {'obj': obj}
    return render(request, 'show-lec.html', context)


def updateview(request, lid):
    obj = Lecturer.objects.get(lid=lid)
    form = LecturerForm(instance=obj)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {
        'form': form
    }
    return render(request, 'lecturer.html', context)


def deleteview(request, lid):
    obj = Lecturer.objects.get(lid=lid)
    if request.method == 'POST':
        obj.delete()
        return redirect('lecshow_url')
    context = {
        'obj': obj
    }
    return render(request, 'confirmationl.html', context)
