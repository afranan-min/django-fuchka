from django.contrib import admin
from .models import Fuchka

class FuchkaAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity')

admin.site.register(Fuchka,FuchkaAdmin)
# Register your models here.
