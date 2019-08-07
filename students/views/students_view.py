from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Student

# Views for Students

def students_list_custom_page(request):
    students = Student.objects.all()

    # order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    else:
        students = students.order_by('last_name')

    # paginate students

    list_len = len(students)
    paginator = 3 # items per page

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    last_item = paginator * page
    first_item = last_item - paginator

    pages = [i + 1 for i in
             range(list_len // paginator + (1 and list_len%paginator != 0))]

    if last_item > list_len:
       # if out of range deliver last page
       students = students[(pages[-2])*paginator : list_len]
    else:
        students = students[first_item:last_item]

    return render(request, 'students/stud_list_custom_page.html', {
                    'students': students,
                    'pages': pages})


def students_list(request):
    students = Student.objects.all()

    # order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    else:
        students = students.order_by('last_name')

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # if page not an integer deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h2>Add student form</h2>')

def students_edit(request, sid):
    return HttpResponse(f'<h2>Edit student {sid}</h2>')

def students_delete(request, sid):
    return HttpResponse(f'<h2>Delete student {sid}</h2>')


