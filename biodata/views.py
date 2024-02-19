from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Student

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def students(request):
    student = Student.objects.all().values()
    context = {
        'student' : student,
    }
    template = loader.get_template('students.html')
    return HttpResponse(template.render(context, request))

def studentdetail(request, student_id):
    # Retrieve the student object with the given ID, or return a 404 error if not found
    student = get_object_or_404(Student, pk=student_id)
    
    # Render the template with the student details
    return render(request, 'studentdetail.html', {'student': student})


def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())
