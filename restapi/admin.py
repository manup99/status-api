from django.contrib import admin
from .models import Status
# Register your models here.
from .forms import StatusForm
class StatusAdmin(admin.ModelAdmin):
    form = StatusForm
admin.site.register(Status, StatusAdmin)