from django.urls import path
from .views import Teacher_RegisterView, Teacher_LoginView, Teacher_LogoutView, StudentView, Student_detailsView, StudentMarkView, StudentMark_details


urlpatterns = [
    path('register/', Teacher_RegisterView.as_view()),
    path('login/', Teacher_LoginView.as_view()),
    path('logout/', Teacher_LogoutView.as_view()),

    path('student/', StudentView.as_view()),
    path('student_details/<int:id>/',Student_detailsView.as_view()),

    path('student_mark/', StudentMarkView.as_view()),
    path('student_mark_details/<int:id>/',StudentMark_details.as_view()),
   
] 