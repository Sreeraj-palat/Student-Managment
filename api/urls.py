from django.urls import path
from .views import Teacher_RegisterView, Student_RegisterView


urlpatterns = [
    path('register/', Teacher_RegisterView.as_view()),
    path('student_register/',Student_RegisterView.as_view()),
   
] 