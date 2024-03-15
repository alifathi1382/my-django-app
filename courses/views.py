from django.shortcuts import render, redirect
from .forms import CoursesForm
from .models import Courses
from django.template import loader


# Create your views here.


def coursesformview(request):
    form = CoursesForm()
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, 'courses.html', context)


def showView(request):
    obj = Courses.objects.all()
    template_path = 'show.html'  # Adjust the template path as per your project structure
    template = loader.get_template(template_path)
    context = {'obj': obj}
    return render(request, 'show.html', context)


def updateview(request, cid):
    obj = Courses.objects.get(cid=cid)
    form = CoursesForm(instance=obj)
    if request.method == 'POST':
        form = CoursesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {
        'form': form
    }
    return render(request, 'courses.html', context)


def deleteview(request, cid):
    obj = Courses.objects.get(cid=cid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    context = {
        'obj': obj
    }
    return render(request, 'confirmation.html', context)

