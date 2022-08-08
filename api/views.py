
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import AccountSerializer_teacher, AccountSerializer_student
from .models import Account



class Teacher_RegisterView(APIView):
    def post(self, request):
        serializer = AccountSerializer_teacher(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        user = AccountSerializer_teacher(Account)
        return Response(serializer.data)



class Student_RegisterView(APIView):
    def post(self, request):
        serializer = AccountSerializer_student(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        user = AccountSerializer_student(Account)
        return Response(serializer.data)

