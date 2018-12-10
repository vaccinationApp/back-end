from rest_framework import serializers
from .models import Department,Employee,EmployeeType

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name','address','coordinate','region')

class EmployeeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ('id','name')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','employeeskey','name','employeetype','department','phone')



