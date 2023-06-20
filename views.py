from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def home(request):
    register_obj=registers.objects.all()
    serializer=registersSerializer(register_obj,many=True)

    return Response({'status':200, 'data':serializer.data})

@api_view(['POST'])
def post_home(request):
    register_obj=registers.objects.all()
    serializer=registersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data
        serializer.save()
    return Response(serializer.data)

#update

@api_view(['POST'])
def update_home(request,id):
    register_obj=registers.objects.get(id=id)
    serializer=registersSerializer(instance=register_obj,data=request.data)
    if serializer.is_valid():
        #serializer.validated_data
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
def delete_home(request,id):
    register_obj=registers.objects.get(id=id)
    register_obj.delete()
    return Response("user deleted successfully")
