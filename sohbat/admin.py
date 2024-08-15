from django.contrib import admin
from .models import LLM, SystemPrompt, Interaction


class ReadOnlyAdmin(admin.ModelAdmin):
    # Disable all editing functionality
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(LLM, ReadOnlyAdmin)
admin.site.register(SystemPrompt, ReadOnlyAdmin)
admin.site.register(Interaction, ReadOnlyAdmin)
