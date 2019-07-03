from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
        {'id': 1,
         'first_name': 'Іван',
         'last_name': 'Окунь',
         'ticket': 5,
         'image': 'img/perch.jpg'},
        {'id': 2,
         'first_name': 'Михайлина',
         'last_name': 'Щука',
         'ticket': 15,
         'image': 'img/pike.jpg'},
        {'id': 3,
         'first_name': 'Дмитро',
         'last_name': 'Судак',
         'ticket': 20,
         'image': 'img/zander.jpeg'}
        )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h2>Add student form</h2>')

def students_edit(request, sid):
    return HttpResponse(f'<h2>Edit student {sid}</h2>')

def students_delete(request, sid):
    return HttpResponse(f'<h2>Delete student {sid}</h2>')


