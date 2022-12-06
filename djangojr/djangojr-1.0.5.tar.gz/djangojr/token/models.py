from django.db import models
from ..utils import generate_hash, settings


class Token(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_hash(32)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.token
