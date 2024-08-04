from django.db import models

# Create your models here.
class LLM(models.Model):
    provider_name = models.CharField(max_length=100)
    model_name_version = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.provider_name} - {self.model_name_version}"
