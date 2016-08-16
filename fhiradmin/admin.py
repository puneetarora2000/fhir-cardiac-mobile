from django.contrib import admin

# Register your models here.


from django import forms
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
import re

from .models import NicotineFood,TypeOfSmoke,PhysicalActivity,DietInTakePerDay,BloodPressureReading,CholesterolReading,UserMedicalProfile

admin.site.register(BloodPressureReading)
admin.site.register(CholesterolReading)
admin.site.register(UserMedicalProfile)


admin.site.register(TypeOfSmoke)
#admin.site.register(NicotineFood)
admin.site.register(PhysicalActivity)
admin.site.register(DietInTakePerDay)



