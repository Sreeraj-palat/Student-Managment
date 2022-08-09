from asyncio import exceptions
from pyexpat import model
from wsgiref import validate
from rest_framework import serializers
from .models import Account, StudentDetails, Student

class AccountSerializer_teacher(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email','username', 'password']

        
    def create(self,validated_data):
        user = Account.objects.create_user(
           email = validated_data['email'],
           first_name = validated_data['first_name'],
           last_name = validated_data['last_name'],
           username = validated_data['username'],
           password = validated_data['password'],
        )        
        user.is_staff = True   
        return user




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'

