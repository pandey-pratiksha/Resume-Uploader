from django.shortcuts import render
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class profileview(APIView):
    def post(request,self,format=None):
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'createsussesfully'})

        return Response(serializer.errors)

    def get(reuest,self,format=None):
        stu=Profile.objects.all()
        serializer=ProfileSerializer(stu,many=True)
        return Response({'status':'sussesfully', 'data':serializer.data})



        
        

