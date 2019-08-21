import time
from django.core import serializers
from celery import shared_task
from ..models import Student


@shared_task
def get_ordered_student_list(request):

    students = Student.objects.all()

    # order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    else:
        students = students.order_by('last_name')

    students = serializers.serialize("json", students)

    return students

@shared_task
def pause_run(a):
    time.sleep(a)
