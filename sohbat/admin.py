from django.contrib import admin
from .models import LLM, SystemPrompt, UserPrompt, Interaction

admin.site.register(LLM)
admin.site.register(SystemPrompt)
admin.site.register(UserPrompt)
admin.site.register(Interaction)
