from django.shortcuts import render
from django.http import HttpResponse

# Attendance View
def attendance(request):
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
    return render(request, 'students/attendance.html', {'students': students})
