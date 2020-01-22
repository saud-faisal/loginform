from django.contrib import admin
from LoginApp.models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','address,','email','password','cpassword']

admin.site.register(Registration)
