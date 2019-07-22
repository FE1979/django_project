from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student

# Views for Students

def students_list(request):
    students = Student.objects.all()

    # order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h2>Add student form</h2>')

def students_edit(request, sid):
    return HttpResponse(f'<h2>Edit student {sid}</h2>')

def students_delete(request, sid):
    return HttpResponse(f'<h2>Delete student {sid}</h2>')


