from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from  .serializers import  StudentSerializer
from .models import Student
from rest_framework.permissions import DjangoModelPermissions,DjangoObjectPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticated
from  rest_framework.authentication import  BasicAuthentication,SessionAuthentication,TokenAuthentication

from .custompermission import MyPermission

from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

from testapi.throttling import  StudentRateThrottle
# from django_filters.rest_framework import DjangoFilterBackend

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import  SearchFilter,OrderingFilter

from .mypagination import StudentViewPagination,MyLimitOffsetPagination




class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_class=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    throttle_class=[AnonRateThrottle,StudentRateThrottle]
    # filter_backends=[DjangoFilterBackend]
    filter_backends=[SearchFilter,OrderingFilter,DjangoFilterBackend]
    search_fields=['$name','=age','$address']#http://host/?search=value
    filterset_fields=['name','age'] #http://host/?fieldname=name&secondfield=name
   
    pagination_class=MyLimitOffsetPagination
    
    ordering_fields=['name','age','address']