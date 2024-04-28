from django.contrib import admin
from authentication.models import Signup

# Register your models here.
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ["username","First_name","Last_name","Email_id","pass1"]


