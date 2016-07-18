from django.contrib.auth.models import User, Group
from fhiradmin.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class NicotineFoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NicotineFood
        fields = ('NicotineFood', 'LastUpdate')

class TypeOfSmokeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeOfSmoke
        fields = ('SmokingMedium', 'LastUpdate')

class PhysicalActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhysicalActivity
        fields = ('PhysicalActivitySpeed', 'LastUpdate')

        #BloodPressureReading
class BloodPressureReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodPressureReading
        fields = ('SystolicReading','DiastolicReading','LastDateOfTest','LastUpdate')

        #DietInTakePerDay
class DietInTakePerDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DietInTakePerDay
        fields = ('WhichDrink','FatInTake','FoodSupliment','LastUpdate')


#CholesterolReading

class CholesterolReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CholesterolReading
        fields = ('LowDensityLipoProtein','VeryLowDensityLipoProtein','HighDensityLipoProtein','TriglyceridesReadings','TotalCholesterol','LastDateOfTest','LastUpdate')
