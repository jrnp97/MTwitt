from django.contrib import admin
from .models import Twitt
# Register your models here.

class t(admin.ModelAdmin):
    list_display = ["__str__","date_twit"]
    class Meta:
        model = Twitt
admin.site.register(Twitt, t)