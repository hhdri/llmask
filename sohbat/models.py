from django.db import models


class LLM(models.Model):
    provider_name = models.CharField(max_length=100, null=False)
    model_name_version = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=100, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["provider_name", "model_name_version"],
                name="unique_provider_model",
            ),
            models.UniqueConstraint(fields=["slug"], name="unique_slug"),
        ]

    def __str__(self):
        return self.slug


class SystemPrompt(models.Model):
    name = models.CharField(max_length=100, null=False)
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["prompt"], name="unique_system_prompt"),
        ]

    def __str__(self):
        return self.name


class UserPrompt(models.Model):
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["prompt"], name="unique_prompt"),
        ]

    def __str__(self):
        return self.prompt


class Interaction(models.Model):
    llm = models.ForeignKey(LLM, on_delete=models.CASCADE)
    system_prompt = models.ForeignKey(SystemPrompt, on_delete=models.CASCADE)
    user_prompt = models.ForeignKey(UserPrompt, on_delete=models.CASCADE)
    response = models.TextField(blank=True, null=True)
    random_seed = models.IntegerField(default=42)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["llm", "system_prompt", "user_prompt", "random_seed"],
                name="unique_interaction",
            ),
        ]
