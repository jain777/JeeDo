from django.contrib import admin
#from company.models import JobOffer, InternshipOffer, JobAdvertisement, InternshipAdvertisement
from .models import ExpertProfile,AspirantProfile
#from .resources import ExpertProfileResource, AspirantProfileResource
#from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
admin.site.register(ExpertProfile)
admin.site.register(AspirantProfile)