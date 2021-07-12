from django.contrib import admin
from .models import PersonalDetails, QualificationDetails, LocationDetails, ProfileDetails
# Register your models here.
MyModels = [PersonalDetails, QualificationDetails, LocationDetails, ProfileDetails]
admin.site.register(MyModels)