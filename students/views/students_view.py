from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Student, Group
from datetime import datetime

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

    # If form was posted
    if request.method == "POST":
        # If cancel button was pressed
        if request.POST.get('add_button') is None:
            # return user to students list
            return HttpResponseRedirect(
                f"{reverse('home')}?status_message=Додавання скасовано")

        # if add button was pressed
        if request.POST.get('add_button') is not None:
            # verify data and collect errors
            errors = {}

            # data validation
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('middle_name')
                   }

            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = "Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = "Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = "Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = \
                    "Введіть коректний формат дати (напр. 31-12-1989)"
                else:
                    data['birthday'] = birthday

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = "Група є обов'язковою"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = "Оберіть коректну групу"
                else:
                    data['student_group'] = \
                    Group.objects.get(pk=student_group)

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # if data is valid save student
            if not errors:
                student = Student(**data)
                student.save()

                # redirect to students list
                return HttpResponseRedirect(
                    f"{reverse('home')}?status_message=Студента успішно додано")

            # if data is not valid
            else:
                # return form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors}
                             )
    # if form was not posted
    else:
        # return initial form
        return render(request, 'students/students_add.html',
                  {'groups': Group.objects.all().order_by('title')})

class StudentUpdateForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        # set form tag atributes
        self.helper.form_action = reverse('students_edit',
                                          kwargs={'pk': kwargs['instance'].id}
                                         )
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form_horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', 'Зберегти', css_class='btn btn-primary'),
            Submit('cancel_button', 'Скасувати', css_class='btn btn-link')
        )


class StudentsUpdateView(UpdateView):

    model = Student
    template_name = 'students/students_edit.html'

    form_class = StudentUpdateForm

    def get_success_url(self):
        return f"{reverse('home')}?status_message=Студента успішно збережено"

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                f"{reverse('home')}?status_message=Редагування студента\
                відмінено")
        else:
            return super(StudentsUpdateView, self).post(request, *args,
                                                        **kwargs)

def students_edit(request, sid):
    return HttpResponse(f'<h2>Edit student {sid}</h2>')

def students_delete(request, sid):
    return HttpResponse(f'<h2>Delete student {sid}</h2>')


