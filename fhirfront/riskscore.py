from django.db import models
from model_utils import Choices
from django.contrib.auth.models import User

from fhiradmin.models import *

class StatusManager(models.Manager):
    @classmethod
    def successful(self):
        return self.get(code=1)
    @classmethod
    def failed(self):
        return self.get(code=0)

class Status(models.Model):
    code = models.IntegerField()
    text = models.CharField(maxlength=255)

    objects = StatusManager()