from django.shortcuts import render
from django.http import HttpResponse

def students_list(request):
    return HttpResponse("""
                        <h1>World</h1>
                        <h2>Hello</h2>
                       """
                       )
