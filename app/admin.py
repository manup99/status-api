from django.contrib import admin
from .models import *
from .forms import UpdateForm
class UpdateAdmin(admin.ModelAdmin):
    form = UpdateForm
admin.site.register(Update, UpdateAdmin)