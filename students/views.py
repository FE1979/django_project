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

# Groups Views
def group_list(request):
    groups = (
        {'id': 1,
         'title': 'Хижаки',
         'head': 'Бичок',},
        {'id': 2,
         'title': 'Біла',
         'head': 'Плотва',},
        {'id': 3,
         'title': 'Морська',
         'head': 'Камбала',}
        )

    return render(request, 'students/groups_list.html', {'groups': groups})

def group_add(request):
    return HttpResponse('<h2>Add group <h2>')

def group_edit(request, gid):
    return HttpResponse(f'<h2>Edit group {gid}</h2>')

def group_delete(request, gid):
    return HttpResponse(f'<h2>Delete group {gid}</h2>')


