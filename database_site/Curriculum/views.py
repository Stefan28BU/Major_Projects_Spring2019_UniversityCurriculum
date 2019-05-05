from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

from .forms import *


def index(request):
    return render(request=request, template_name="index.html")


def newCurriculum(request):

    if request.method == 'POST':
        form = newCurriculumForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            print('Invalid')
            return HttpResponseRedirect('/Curriculum')
    else:
        form = newCurriculumForm()

    return render(request=request, template_name="curriculum/newCurriculum.html", context={"form": form})


def newHead(request):
    if request.method == 'POST':
        form = headForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            print('Invalid')
            return HttpResponseRedirect('/Curriculum')
    else:
        form = headForm()

    return render(request=request, template_name="curriculum/departmentHead.html", context={"form": form})


def newCourse(request):
    if request.method == 'POST':
        form = newCourseForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            print('Invalid')
            return HttpResponseRedirect('/Curriculum')
    else:
        form = newCourseForm()

    return render(request=request, template_name="curriculum/newCourse.html", context={"form": form})


def newTopic(request):
    if request.method == 'POST':
        form = newTopicForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            print('Invalid')
            return HttpResponseRedirect('/Curriculum')
    else:
        form = newTopicForm()

    return render(request=request, template_name="curriculum/newTopic.html", context={"form": form})


def newGoal(request):
    if request.method == 'POST':
        form = newGoalForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            print('Invalid')
            return HttpResponseRedirect('/Curriculum')
    else:
        form = newGoalForm()

    return render(request=request, template_name="curriculum/newGoal.html", context={"form": form})

def dashboard(request):
    curricula = Curriculum.objects.order_by('-Cur_name')[:5]
    output = ', '.join([c.Cur_name for c in curricula])
    return HttpResponse(output)


def editPerson(request):
    if request.method == 'POST':
        form = editPersonForm(request.POST)

        if form.is_valid():
            temp = Person.objects.get(ID=form['curr'].value())

            temp.Name = form['name'].value()
            temp.save()

            print("person ", temp.Name)

        else:
            print('Invalid')
            return HttpResponseRedirect('/Curriculum')
    else:
        form = editPersonForm()

    return render(request=request, template_name="Edit/editPerson.html", context={"form": form})


def editCurriculum(request):
    if request.method == 'POST':
        form = editCurriculumFrom(request.POST)

        if form.is_valid():
            temp = Curriculum.objects.get(Cur_name=form['curr'].value())
            tempPerson = Person.objects.get(ID=form['newHead'].value())

            temp.Head = tempPerson
            temp.Min_Hours = form['newHours'].value()

            temp.save()


        else:
            print('Invalid')
            return HttpResponseRedirect('/Curriculum')
    else:
        form = editCurriculumFrom()

    return render(request=request, template_name="Edit/editCurriculum.html", context={"form": form})
