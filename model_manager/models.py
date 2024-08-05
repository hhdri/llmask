from django.db import models

# Create your models here.
# class LLM(models.Model):
#     provider_name = models.CharField(max_length=100, null=False)
#     model_name_version = models.CharField(max_length=100, null=False)
#     slug = models.CharField(max_length=100, null=False)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['provider_name', 'model_name_version'], name='unique_provider_model'),
#             models.UniqueConstraint(fields=['slug'], name='unique_slug'),
#         ]

#     def __str__(self):
#         return f"{self.provider_name} - {self.model_name_version}"
