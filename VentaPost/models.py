from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(default='batman.png')

    def __str__(self):
        return f'Pefil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self) -> str:
        return f'{self.user.username}: {self.content}'