from Tkinter import Radiobutton

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(RiskLabels)
admin.site.register(RiskScore)


admin.site.register(Agerisk)
admin.site.register(Alcoholrisk)

admin.site.register(BloodPressureRisk)
admin.site.register(CholesterolRisk)

admin.site.register(Dietrisk)
admin.site.register(Hormonalrisk)

admin.site.register(Physicalactivityrisk)
admin.site.register(Sexrisk)

admin.site.register(Weightrisk)
admin.site.register(Smokingrisk)