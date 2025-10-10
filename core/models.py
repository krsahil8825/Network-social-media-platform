from django.db import models
from users.models import User

# Create your models here.
class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.user.username if self.user else 'Anonymous'}: {self.subject:.20}..."