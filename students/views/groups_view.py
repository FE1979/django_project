from django.shortcuts import render
from django.http import HttpResponse

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


