from django.contrib import admin

# Register your models here.
from django.contrib import admin
from lps.models import FreeConsultationModel


@admin.register(FreeConsultationModel)
class FreeConsultationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    FreeConsultationModel._meta.get_fields()]