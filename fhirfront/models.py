from __future__ import unicode_literals

from django.db import models
from model_utils import Choices


class RiskLabels(models.Model):
    RiskChoices = Choices('negligible','low','moderate','high','certain')
    RiskGroups = models.CharField(choices=RiskChoices, default=RiskChoices.low, max_length=20)
    LastUpdate = models.DateTimeField(auto_now_add=True)


class RiskScore(models.Model):
    RiskChoices = Choices('negligible','low','moderate','high','certain')
    DietScore = models.IntegerField(verbose_name='LifeStyleScore',default=0)
    BloodPressureScore = models.IntegerField(verbose_name='LifeStyleScore',default=0)
    CholesterolScore = models.IntegerField(verbose_name='LifeStyleScore',default=0)
    PhysicalActivity = models.IntegerField(verbose_name='PhysicalActivity Score',default=0)
    SmokeScore = models.IntegerField(verbose_name='Smoke Score',default=0)
    TotalScore = models.IntegerField(verbose_name='TotalScore',default=0)
    Outcome = models.OneToOneField(RiskLabels,verbose_name='OutCome',default=RiskLabels.RiskGroups)
    User = models.OneToOneField(User,verbose_name='Full Name:',default='1')
    LastUpdate = models.DateTimeField(auto_now_add=True)