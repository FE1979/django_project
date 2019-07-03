"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Students urls
    re_path(r'^$', views.students_list, name='home'),
    re_path(r'^students/add$', views.students_add, name='students_add'),
    re_path(r'^students/(?P<sid>\d+)/edit$', views.students_edit,
            name='students_edit'),
    re_path(r'^students/(?P<sid>\d+)/delete$', views.students_delete,
            name='students_delete'),

    # Groups urls
    re_path(r'^groups/$', views.group_list, name='group_home'),
    re_path(r'^groups/add$', views.group_add, name='group_add'),
    re_path(r'^groups/(?P<gid>\d+)/edit$', views.group_edit,
            name='group_edit'),
    re_path(r'^groups/(?P<gid>\d+)/delete$', views.group_delete,
            name='group_delete'),
    # Attendance urls
    re_path(r'^journal', views.attendance, name='attendance'),
]
