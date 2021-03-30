from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Person, Activity
from .resources import PersonResource, ActivityResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
# Crud
from django.shortcuts import render, redirect

from django.core.paginator import Paginator

import time


@login_required
def simple_upload(request):
    if request.method == 'POST':
        start_time = time.time()
        person_resource = PersonResource()
        activity_resource = ActivityResource()
        activity = Activity()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        if not new_persons.name.endswith('xlsx'):
            messages.info(request, '❌ - Wrong format type, Please choose another one and try again, e.g (xlsx)')
            return render(request, 'hello/upload.html')

        imported_data = dataset.load(new_persons.read(), format='xlsx')
        messages.info(request, '✅ - Your file added successfully')
        tot = 0
        for data in imported_data:
            tot = tot + 1
            value = Person(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],

            )

            value.save()
            activity.name = new_persons.name
            activity.records = tot
            activity.execution = ((time.time()) - start_time)
          # datetime.datetime.now().strftime("%Y%m%d")
            activity.save()

    return render(request, 'hello/upload.html')


def activity(request):
    activity = Activity.objects.all()
    return render(request, 'hello/activity.html', {'activity': activity})


# Create your views here.
@login_required
def index(request):
    return render(request, 'hello/index.html')


@login_required
def indexForm(request):
    return render(request, 'hello/form.html')


@login_required
def indexTable(request):
    return render(request, 'hello/table.html')


def handler404(request, *args, **argv):
    return redirect('home')


#################
# start CRUD.
#################



@login_required
def show(request):
    if 'q' in request.GET:
        q = request.GET['q']
        persons = Person.objects.filter(name=q)
    else:
      
        persons = Person.objects.all()
        paginator = Paginator(persons, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="hello/table.html", context={'persons': page_obj})

@login_required
def new(request):
    return render(request, 'hello/add.html')


@login_required
def add(request):

    person = Person()
    person.name = request.POST['name']
    person.email = request.POST['email']
    person.age = request.POST['age']
    person.height = request.POST['height']
    person.city = request.POST['city']
    person.average_earning = request.POST['average_earning']
    person.clothes_expenses = request.POST['clothes_expenses']
    person.creams_expenses = request.POST['creams_expenses']
    person.save()
    # anas = Person.objects.last()
    return redirect('/table')


@login_required
def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'hello/edit.html', {'person': person})


@login_required
def update(request, id):
    person = Person.objects.get(id=id)
    person.name = request.POST['name']
    person.email = request.POST['email']
    person.age = request.POST['age']
    person.height = request.POST['height']
    person.city = request.POST['city']
    person.average_earning = request.POST['average_earning']
    person.clothes_expenses = request.POST['clothes_expenses']
    person.creams_expenses = request.POST['creams_expenses']
    person.save()
    return redirect('/table')


@login_required
def destroy(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("/table")


@login_required
def chart(request):
    context = {
        "person": Person.objects.all(),
        "topTen": Person.objects.order_by('-average_earning')[:10],
        "topfiften": Person.objects.order_by('-clothes_expenses')[:10],
    }
    return render(request, 'hello/chart.html', context)


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        persons = Person.objects.filter(name=q)
    else:
        persons = Person.objects.all()

    return render(request, 'hello/search.html', {'persons': persons})



#
# def header(request):
#     return render(request, 'hello/include/header.html')