from django.contrib import admin

# Register your models here.
from .models import Parcial, Talleres, Apuntes

admin.site.register(Parcial)
admin.site.register(Talleres)
admin.site.register(Apuntes)