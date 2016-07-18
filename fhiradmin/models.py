from __future__ import unicode_literals

from django.db import models
#from model_utils.fields import MonitorField, StatusField
from model_utils import Choices
# Create your models here.
#from django.contrib.admin import AdminSite

from django.contrib.auth.models import User




class UserMedicalProfile(models.Model):
    SexChoice = Choices('Male','Female','Transgender')
    FamilyHistoryChoices = Choices('Yes','No','Unknown')
    HormonalFactorChoices = Choices('Yes','No','Unknown')
    Subject = models.OneToOneField(User,verbose_name = 'Full Name:',default='1')
    Age = models.IntegerField(default='20', verbose_name='Age :')
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Male, max_length=20)
    FamilyHistory = models.CharField(choices=HormonalFactorChoices, default=FamilyHistoryChoices.No, max_length=20)
    Weight = models.IntegerField(default='50', verbose_name='Weight in Kgs')
    HormonalFactor =models.CharField(choices=HormonalFactorChoices, default=HormonalFactorChoices.No, max_length=20)
    LastUpdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.User

class TypeOfSmoke(models.Model):
    User = models.OneToOneField(User,verbose_name='Full Name:',default='1')
    SmokingMedium  = models.CharField(max_length=100,default='Cigrate/Nicotine',verbose_name='SmokingMedium')
    SmokingMedium  = models.CharField(max_length=100,default='Cigrate/Nicotine',verbose_name='SmokingMedium')
    LastUpdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.SmokingMedium


class NicotineFood(models.Model):
    NictineChoices = Choices(('Sugar Drinks per Day', ['No', 'Negligible']),('Alcohol Drinks per Day', ['Rare','Once', 'Twice','Thrice','Thrice','More than 3 times']),('Juices per Day', ['Natual', 'Artifical Falavored']),('Herbal Drinks', ['Rare','Once', 'Twice','Thrice','Thrice','More than 3 times']),('WaterInTake', ['3 Glasses', '5 Glasses','7 Glasses','>7 Glasses']), ('XXX', ['Slow', 'Medium','Fast']))
    User = models.OneToOneField(User,verbose_name='Full Name:',default='1')
    NicotineFood  = models.CharField(choices=NictineChoices,max_length=100,default=NictineChoices.No,verbose_name='NicotineFood')
    LastUpdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.NicotineFood

class PhysicalActivity(models.Model):
    User = models.OneToOneField(User,verbose_name='Full Name:',default='1')
    SpeedChoices = Choices(('Meditation', ['10 Min', '20 Min','>20 Min']),('Physical-Exercise', ['No', 'Negligible']),('Cycling', ['Slow', 'Medium','Fast']),('Dance', ['Slow', 'Medium','Fast']),('Yoga', ['Slow', 'Medium','Fast']),('Walking', ['Slow', 'Medium','Fast']), ('Jogging-Running', ['Slow', 'Medium','Fast']))
    PhysicalActivitySpeed = models.CharField(choices=SpeedChoices, default=SpeedChoices.Slow, max_length=20)
    LastUpdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.PhysicalActivitySpeed

class DietInTakePerDay(models.Model):
    User = models.OneToOneField(User,verbose_name='Full Name:',default='1')
    Drinks = Choices(('Sugar Drinks per Day', ['No', 'Negligible']),('Alcohol Drinks per Day', ['Rare','Once', 'Twice','Thrice','Thrice','More than 3 times']),('Juices per Day', ['Natual', 'Artifical Falavored']),('Herbal Drinks', ['Rare','Once', 'Twice','Thrice','Thrice','More than 3 times']),('WaterInTake', ['3 Glasses', '5 Glasses','7 Glasses','>7 Glasses']), ('XXX', ['Slow', 'Medium','Fast']))
    Fats = Choices(('Sugar Drinks per Day', ['No', 'Negligible']),('Alcohol Drinks per Day', ['Rare','Once', 'Twice','Thrice','Thrice','More than 3 times']),('Juices per Day', ['Natual', 'Artifical Falavored']),('Herbal Drinks', ['Rare','Once', 'Twice','Thrice','Thrice','More than 3 times']),('WaterInTake', ['3 Glasses', '5 Glasses','7 Glasses','>7 Glasses']), ('XXX', ['Slow', 'Medium','Fast']))
    Supliment = Choices(('Sugar Drinks per Day', ['No', 'Negligible']),('Alcohol Drinks per Day', ['Rare','Once', 'Twice','Thrice','Thrice','More than 3 times']),('Juices per Day', ['Natual', 'Artifical Falavored']),('Herbal Drinks', ['Rare','Once', 'Twice','Thrice','Thrice','More than 3 times']),('WaterInTake', ['3 Glasses', '5 Glasses','7 Glasses','>7 Glasses']), ('XXX', ['Slow', 'Medium','Fast']))
    WhichDrink = models.CharField(choices=Drinks, default=Drinks.Slow, max_length=20)
    FatInTake = models.CharField(choices=Fats, default=Drinks.Slow, max_length=20)
    FoodSupliment = models.CharField(choices=Supliment, default=Drinks.Slow, max_length=20)
    LastUpdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Drinks



    #Systolic and Diastolic Blood Pressure
class BloodPressureReading(models.Model):
    CaffeineChoices = Choices('Yes','No','Unknown')
    User = models.OneToOneField(User,verbose_name='Full Name:',default='1')
    SystolicReading  =  models.IntegerField(default='90',verbose_name='Systolic Reading')
    DiastolicReading  = models.IntegerField(default='100',verbose_name='Diastolic   Reading')
    isCaffeineConsumer = models.CharField(choices=CaffeineChoices, default=CaffeineChoices.No, max_length=20)
    LastDateOfTest = models.DateTimeField()
    LastUpdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Drinks

class CholesterolReading(models.Model):
    User = models.OneToOneField(User,verbose_name='Full Name:',default='1')
    LowDensityLipoProtein =models.IntegerField(default='90',verbose_name='L D L ')
    HighDensityLipoProtein = models.IntegerField(default='90',verbose_name='H D L ')
    VeryLowDensityLipoProtein = models.IntegerField(default='90',verbose_name='VLDL')
    TriglyceridesReadings = models.IntegerField(default='90',verbose_name='Triglycerides')
    TotalCholesterol=models.IntegerField(default='90',verbose_name='Total Cholesterol')
    LastDateOfTest = models.DateTimeField()
    LastUpdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Drinks







