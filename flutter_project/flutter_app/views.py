from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EventPage , RaiseHand , RequestInsitute , InstituteDetails , EditProfile
from .serializer import DataSerializer , RequestInsituteSerializer ,   InstituteDetailsSerializer , EditProfileSerializer
from django.views.generic.edit import UpdateView
from rest_framework import generics
@api_view(['GET'])
def getData(request):
    app = EventPage.objects.all()
    serializer = DataSerializer(app,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def getInsituteName(request):
    serializer = RequestInsituteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getInstituteDetails(request):
    app = InstituteDetails.objects.all()
    serializer = InstituteDetailsSerializer(app,many= True)
    return Response(serializer.data)

@api_view(['POST'])
def postInstituteDetails(request):
    serializer = InstituteDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getprofile(request):
    app = EditProfile.objects.all()
    serializer = EditProfileSerializer(app,many=True)
    return Response(serializer.data)









        


