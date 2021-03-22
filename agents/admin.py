from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hired_on')
    list_display_links = ('id', 'name')
    list_per_page = 10

admin.site.register(Agent, AgentAdmin)