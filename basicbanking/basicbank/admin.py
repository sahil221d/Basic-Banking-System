from django.contrib import admin
from django.dispatch import receiver
from .models import Users,Transfer
# Register your models here.

@admin.register(Users)
class users(admin.ModelAdmin):
    list_display = ['accno','name','email','accbal']    


@admin.register(Transfer)
class transfer(admin.ModelAdmin):
    list_display = ['sender', 'amount', 'receiver', 'datetrans']
