from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        AllowAny,
                                        )
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_202_ACCEPTED,
                                   )
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

class StudentsList(APIView):

    permission_classes = (AllowAny,)

    def get(self, requset, *args, **kwargs):   
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    

    def post(self, request, *arg, **kwargs):
       
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    


    

class StudentDetails(APIView):

    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            instance = Student.objects.get(id=pk)
            print('HOH',instance)
            serializer = StudentSerializer(instance)
            return Response(serializer.data, status=HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'details':'Student not found!'}, status = HTTP_400_BAD_REQUEST)

    def delete(self, request, *arg, **kwargs):
        pk = kwargs.get('pk')
        
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return Response({'details':'Student was delited!'}, status = HTTP_202_ACCEPTED)

        except Student.DoesNotExist:
            return Response({'details':'Student not found!'}, status = HTTP_400_BAD_REQUEST)
         
        

    def put(self, request, *arg, **kwargs):
        pk = kwargs.get('pk')
       
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
                
        except Student.DoesNotExist:
            return Response({'details':'Student not found!'}, status = HTTP_400_BAD_REQUEST)
    