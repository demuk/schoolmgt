from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('signup/', views.signup, name="signup"),
]