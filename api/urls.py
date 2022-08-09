from django.urls import path
from .views import Teacher_RegisterView, Teacher_LoginView, Teacher_LogoutView, StudentView, Student_detailsView, StudentMarkView, StudentMark_details


urlpatterns = [
    path('register/', Teacher_RegisterView.as_view()),#register teacher
    path('login/', Teacher_LoginView.as_view()),#teacher login
    path('logout/', Teacher_LogoutView.as_view()),#teacher logout

    path('student/', StudentView.as_view()),#create and view  student
    path('student_details/<int:id>/',Student_detailsView.as_view()),#single student details

    path('student_mark/', StudentMarkView.as_view()),#create and view marklist
    path('student_mark_details/<int:id>/',StudentMark_details.as_view()),#single marklist details 
   
] 