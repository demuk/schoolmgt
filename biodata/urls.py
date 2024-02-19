from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path("studentdetail/<student_id>", views.studentdetail, name="studentdetail"),
    path('signup/', views.signup, name="signup"),
]