from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_date']


@admin.register(PlanProgram)
class PlanProgramAdmin(admin.ModelAdmin):
    list_display = ['plan', 'program']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['client', 'plan', 'date_start', 'date_end']