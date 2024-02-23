from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
    # Number of visits to this view
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits' : num_visits,
    }
    return render(request, 'home.html', context=context)

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'registration.html', {'form': form})


def students(request):
    student = Student.objects.all()
    context = {
        'student' : student,
    }
    return render(request, 'students.html', context)

def studentdetail(request, student_id):
    # Retrieve the student object with the given ID, or return a 404 error if not found
    student = get_object_or_404(Student, pk=student_id)
    
    # Render the template with the student details
    return render(request, 'studentdetail.html', {'student': student})


def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())
    

