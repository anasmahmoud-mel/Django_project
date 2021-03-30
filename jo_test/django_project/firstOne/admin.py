from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Person


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'email', 'age', 'height', 'average_earning', 'clothes_expenses', 'makeup_expenses', 'creams_expenses', 'note')

# Register your models here.
