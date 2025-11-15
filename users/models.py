from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom user model abstracting from AbstractUser
class User(AbstractUser):
    pass


# Model to represent following relationships between users
class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"


# Model to represent user profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
