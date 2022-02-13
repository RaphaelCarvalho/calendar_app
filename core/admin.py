from django.contrib import admin
from core.models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_event', 'date_creation')
    list_filter = ('user',)

admin.site.register(Event, EventAdmin)