from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Bank_ind)
admin.site.register(Bank_legal)
admin.site.register(Bank_corp)
