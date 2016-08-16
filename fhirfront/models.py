from __future__ import unicode_literals

from django.db import models
from model_utils import Choices
from django.contrib.auth.models import User

class RiskLabels(models.Model):
    RiskChoices = Choices('negligible','low','moderate','high','certain')
    RiskGroups = models.CharField(choices=RiskChoices, default=RiskChoices.low, max_length=20)
    LastUpdate = models.DateTimeField(auto_now_add=True)
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

class RiskScore(models.Model):
    RiskChoices = Choices('negligible','low','moderate','high','certain')
    DietScore = models.IntegerField(verbose_name='LifeStyleScore',default=0)
    BloodPressureScore = models.IntegerField(verbose_name='LifeStyleScore',default=0)
    CholesterolScore = models.IntegerField(verbose_name='LifeStyleScore',default=0)
    PhysicalActivity = models.IntegerField(verbose_name='PhysicalActivity Score',default=0)
    SmokeScore = models.IntegerField(verbose_name='Smoke Score',default=0)
    TotalScore = models.IntegerField(verbose_name='TotalScore',default=0)
    Outcome = models.OneToOneField(RiskLabels,verbose_name='OutCome',default=RiskLabels.RiskChoices.low)
    User = models.OneToOneField(User,verbose_name='Full Name:',default='1')
    LastUpdate = models.DateTimeField(auto_now_add=True)
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

    #http://stackoverflow.com/questions/19595067/git-add-commit-and-push-commands-in-one


class Agerisk(models.Model):
    SexChoice = Choices('Male','Female','Transgender')
    agegroup = models.CharField(db_column='AgeGroup', max_length=200, blank=True, null=True)  # Field name made lowercase.
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Male, max_length=20)  # Field name made lowercase.
    weightrange = models.CharField(db_column='WeightRange', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviation = models.FloatField(db_column='FirstStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    firstscore = models.FloatField(db_column='FirstScore', blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.FloatField(db_column='SecondStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    secondscore = models.FloatField(db_column='SecondScore', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.FloatField(db_column='ThirdStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    thirdscore = models.FloatField(db_column='thirdscore', blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'agerisk'


class Alcoholrisk(models.Model):
    SexChoice = Choices('Male','Female','Transgender')
   # id = models.IntegerField(blank=True, null=True)
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Male, max_length=20) # Field name made lowercase.
    frequencyofalcoholintake = models.CharField(db_column='FrequencyofAlcoholinTake', max_length=200, blank=True, null=True)  # Field name made lowercase.
    noofdrinksrange = models.CharField(db_column='NoOfDrinksRange', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviation = models.FloatField(db_column='FirstStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    firstscore = models.FloatField(db_column='FirstScore', blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.FloatField(db_column='SecondStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    secondscore = models.FloatField(db_column='SecondScore', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.FloatField(db_column='ThirdStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    thirdscore = models.FloatField(db_column='thirdscore', blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'alcoholrisk'


class BloodPressureRisk(models.Model):
    SexChoice = Choices('Male','Female','Same')
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Male, max_length=20)
    riskcategory = models.CharField(db_column='RiskCategory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    systolicreading = models.CharField(db_column='SystolicReading', max_length=200, blank=True, null=True)  # Field name made lowercase.
    diastolicreading = models.CharField(db_column='DiastolicReading', max_length=200, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'bloodpressurerisk'


class CholesterolRisk(models.Model):
   # id = models.AutoField()
    SexChoice = Choices('Male','Female','Same')
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Male, max_length=20)
    riskcategory = models.CharField(db_column='RiskCategory', max_length=300, blank=True, null=True)  # Field name made lowercase.
    cholesterolreadings = models.CharField(db_column='CholesterolReadings', max_length=300, blank=True, null=True)  # Field name made lowercase.
    mean = models.CharField(db_column='Mean', max_length=300, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviation = models.CharField(db_column='FirstStandardDeviation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviationscore = models.CharField(db_column='FirstStandardDeviationScore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.CharField(db_column='SecondStandardDeviation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviationscore = models.CharField(db_column='SecondStandardDeviationScore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.CharField(db_column='ThirdStandardDeviation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviationscore = models.CharField(db_column='ThirdStandardDeviationScore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'CholesterolRisk'


class Hormonalrisk(models.Model):
    #id = models.AutoField()
    SexChoice = Choices('Male','Female','Same')
    hormonalcomplicationscategory = models.CharField(db_column='HormonalComplicationsCategory', max_length=300, blank=True, null=True)  # Field name made lowercase.
    AgeRange = models.CharField(db_column='AgeRange', max_length=300, blank=True, null=True)  # Field name made lowercase.
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Same, max_length=20)  # Field name made lowercase.
   # Calorierange = models.CharField(db_column='Calorierange', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mean = models.FloatField(db_column='Mean', blank=True, null=True)  # Field name made lowercase.
    firststandarddeviation = models.CharField(db_column='FirstStandardDeviation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviationscore = models.CharField(db_column='FirstStandardDeviationScore', max_length=200, blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.CharField(db_column='SecondStandardDeviation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviationscore = models.CharField(db_column='SecondStandardDeviationScore', max_length=200, blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.CharField(db_column='ThirdStandardDeviation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviationscore = models.CharField(db_column='ThirdStandardDeviationScore', max_length=200, blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'hormonalrisk'



class Dietrisk(models.Model):
  #  id = models.AutoField()
    SexChoice = Choices('Male','Female','Same')
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Female, max_length=20)
    dietcategory = models.CharField(db_column='DietCategory', max_length=300, blank=True, null=True)  # Field name made lowercase.
    noofpersons = models.CharField(db_column='NoofPersons', max_length=300, blank=True, null=True)  # Field name made lowercase.
    noofcalories = models.CharField(db_column='NoOfCalories', max_length=300, blank=True, null=True)  # Field name made lowercase.
    mean = models.CharField(db_column='Mean', max_length=300, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviation = models.CharField(db_column='FirstStandardDeviation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviationscore = models.CharField(db_column='FirstStandardDeviationScore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.CharField(db_column='SecondStandardDeviation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviationscore = models.CharField(db_column='SecondStandardDeviationScore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.CharField(db_column='ThirdStandardDeviation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviationscore = models.CharField(db_column='ThirdStandardDeviationScore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'dietrisk'


class Physicalactivityrisk(models.Model):
    SexChoice = Choices('Male','Female','Same')
    physicalactivitycategory = models.CharField(db_column='PhysicalActivityCategory', max_length=299, blank=True, null=True)  # Field name made lowercase.
    TimePeriod = models.CharField(db_column='TimePeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Female, max_length=20)  # Field name made lowercase.
    Frequency = models.CharField(db_column='Frequency', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviation = models.FloatField(db_column='FirstStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    firstscore = models.FloatField(db_column='FirstScore', blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.FloatField(db_column='SecondStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    secondscore = models.FloatField(db_column='SecondScore', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.FloatField(db_column='ThirdStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviationscore = models.CharField(db_column='thirdstandarddeviationscore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'physicalactivityrisk'


class Sexrisk(models.Model):
    SexChoice = Choices('Male','Female','Transgender')
    Frequency = models.CharField(db_column='Frequency', max_length=200, blank=True, null=True,)  # Field name made lowercase.
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Female, max_length=20)  # Field name made lowercase.
    firststandarddeviation = models.FloatField(db_column='FirstStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    firstscore = models.FloatField(db_column='FirstScore', blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.FloatField(db_column='SecondStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    secondscore = models.FloatField(db_column='SecondScore', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.FloatField(db_column='ThirdStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviationscore = models.CharField(db_column='thirdstandarddeviationscore', max_length=300, blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'sexrisk'


class Smokingrisk(models.Model):
   # id = models.AutoField()
    SexChoice = Choices('Male','Female','Same')
    SmokeChoice = Choices('Active','Passive')
    smokingtype = models.CharField(choices=SmokeChoice, default=SmokeChoice.Active, max_length=20)
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Same, max_length=20)
    noofcigarette = models.CharField(db_column='NoOfCigarette', max_length=200, blank=True, null=True)  # Field name made lowercase.
    frequency_time_slot = models.CharField(db_column='Frequency-Time-Slot', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    PercentageSmokerRange = models.CharField(db_column='PercentageSmokerRange', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
   # smokingtype = models.CharField(db_column='SmokingType', max_length=7, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviation = models.FloatField(db_column='FirstStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    firststandarddeviationscore = models.FloatField(db_column='FirstStandardDeviationScore', blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.FloatField(db_column='SecondStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviationscore = models.FloatField(db_column='SecondStandardDeviationScore', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.FloatField(db_column='ThirdStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviationscore = models.FloatField(db_column='ThirdStandardDeviationScore', blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'smokingrisk'


class Weightrisk(models.Model):
    SexChoice = Choices('Male','Female','Same')
    weightcategory = models.CharField(db_column='WeightCategory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    Sex = models.CharField(choices=SexChoice, default=SexChoice.Same, max_length=20) # Field name made lowercase.
    bmi = models.CharField(db_column='BMI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firststandarddeviation = models.FloatField(db_column='FirstStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    firstscore = models.FloatField(db_column='FirstScore', blank=True, null=True)  # Field name made lowercase.
    secondstandarddeviation = models.FloatField(db_column='SecondStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    secondscore = models.FloatField(db_column='SecondScore', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviation = models.FloatField(db_column='ThirdStandardDeviation', blank=True, null=True)  # Field name made lowercase.
    thirdstandarddeviationscore = models.FloatField(db_column='ThirdStandardDeviationScore', blank=True, null=True)  # Field name made lowercase.
    documentation = models.CharField(db_column='Documentation', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'weightrisk'
