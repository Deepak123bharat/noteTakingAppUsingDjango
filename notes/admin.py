from django.contrib import admin

# Register your models here.
from .models import List

class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = List

admin.site.register(List,NoteAdmin)