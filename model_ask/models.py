from django.db import models
from model_manager.models import LLM

class Interaction(models.Model):
    llm = models.ForeignKey(LLM, on_delete=models.CASCADE)
    prompt = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

