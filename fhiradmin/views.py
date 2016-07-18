from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from fhiradmin.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class NicotineFoodViewSet(viewsets.ModelViewSet):

    queryset = NicotineFood.objects.all()
    serializer_class = NicotineFoodSerializer

class  TypeOfSmokeViewSet(viewsets.ModelViewSet):

    queryset = TypeOfSmoke.objects.all()
    serializer_class = TypeOfSmokeSerializer

class  PhysicalActivityViewSet(viewsets.ModelViewSet):
    queryset = PhysicalActivity.objects.all()
    serializer_class = PhysicalActivitySerializer

class  BloodPressureReadingViewSet(viewsets.ModelViewSet):
    queryset = BloodPressureReading.objects.all()
    serializer_class = BloodPressureReading

class  DietInTakePerDayViewSet(viewsets.ModelViewSet):
    queryset = DietInTakePerDay.objects.all()
    serializer_class = DietInTakePerDaySerializer

class CholesterolReadingViewSet(viewsets.ModelViewSet):
    queryset = CholesterolReading.objects.all()
    serializer_class = CholesterolReadingSerializer
