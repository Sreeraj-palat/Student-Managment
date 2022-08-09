
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import AccountSerializer_teacher, StudentDetailsSerializer, StudentSerializer
from .models import Account, Student, StudentDetails
from django.http import HttpResponse, JsonResponse
from rest_framework import status
import jwt, datetime



#Teacher registation view
class Teacher_RegisterView(APIView):
    def post(self, request):
        serializer = AccountSerializer_teacher(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        user = AccountSerializer_teacher(Account)
        return Response(serializer.data)



#Teacher login View
class Teacher_LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Account.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')


        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt':token
        }
        return response



#Teacher logout view
class Teacher_LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response   





class StudentView(APIView):

    #get the list of all students
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)


    #create a new student
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            


  


class Student_detailsView(APIView):
    def get_object(self,id):
        try:
            return Student.objects.get(id=id)

        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    #get single student details
    def get(self,request,id):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)



    #update the single student details
    def put(self, request, id):
        student = self.get_object(id) 
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    #delete single student
    def delete(self, request, id):
        student = self.get_object(id) 
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class StudentMarkView(APIView):

    #get the mark list of all students
    def get(self,request):
        marks = StudentDetails.objects.all()
        serializer = StudentDetailsSerializer(marks,many=True)
        return Response(serializer.data)


    #create a new mark list
    def post(self,request):
        serializer = StudentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    





class StudentMark_details(APIView):
    def get_object(self,id):
        try:
            return StudentDetails.objects.get(id=id)

        except StudentDetails.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #get one by one mark list
    def get(self,request,id):
        student = self.get_object(id)
        serializer = StudentDetailsSerializer(student)
        return Response(serializer.data)


    #update the marklist
    def put(self, request, id):
        student = self.get_object(id) 
        serializer = StudentDetailsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    #delete the mark list
    def delete(self, request, id):
        student = self.get_object(id) 
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            



