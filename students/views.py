from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    return render(request, 'students/students_list.html', {})

def students_add(request):
    return HttpResponse('<h2>Add student form</h2>')

def students_edit(request, sid):
    return HttpResponse(f'<h2>Edit student {sid}</h2>')

def students_delete(request, sid):
    return HttpResponse(f'<h2>Delete student {sid}</h2>')

# Groups Views
def group_list(request):
    return render(request, 'groups/groups_list.html', {})

def group_add(request):
    return HttpResponse('<h2>Add group <h2>')

def group_edit(request, gid):
    return HttpResponse(f'<h2>Edit group {gid}</h2>')

def group_delete(request, gid):
    return HttpResponse(f'<h2>Delete group {gid}</h2>')


