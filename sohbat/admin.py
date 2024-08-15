from django.contrib import admin
from .models import LLM, SystemPrompt, Interaction

admin.site.register(LLM)
admin.site.register(SystemPrompt)
admin.site.register(Interaction)
