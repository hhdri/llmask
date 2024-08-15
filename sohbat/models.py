from django.db import models


class LLM(models.Model):
    provider_name = models.CharField(max_length=100, null=False)
    model_name_version = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=100, null=False, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["provider_name", "model_name_version"],
                name="unique_provider_model",
            )
        ]

    def __str__(self):
        return self.slug


class SystemPrompt(models.Model):
    name = models.CharField(max_length=100, null=False)
    prompt = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Interaction(models.Model):
    llm = models.ForeignKey(LLM, on_delete=models.CASCADE)
    system_prompt = models.ForeignKey(SystemPrompt, on_delete=models.CASCADE)
    user_prompt = models.TextField(blank=False, null=False)
    response = models.TextField(blank=True, null=True)
    random_seed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["llm", "system_prompt", "user_prompt", "random_seed"],
                name="unique_interaction",
            ),
        ]

    def __str__(self):
        return f"{self.llm} - {self.system_prompt} - {self.user_prompt}"
