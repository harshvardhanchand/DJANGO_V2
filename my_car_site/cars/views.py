from django.shortcuts import render, redirect
from django.urls import reverse
from .import models
# Create your views here.


def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}

    return render(request, 'cars/list.html', context=context)


def add(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        year = int(request.POST.get('year'))
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')


def delete(request):
    if request.method == 'POST':
        pk = request.POST['id']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except models.Car.DoesNotExist:
            print('Car does not exist')
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')
