from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def studentdetails(request):
    student = Student.objects.all().values()
    context = {
        'student': student,
    }
    template = loader.get_template('studentdetails.html')
    return HttpResponse(template.render(context, request))