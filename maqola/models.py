from users.models import Profile
from django.db import models
from django.utils import timezone

# Create your models here.

class Maqola(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=70)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='maqolalar')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    maqola = models.ForeignKey('Maqola', on_delete=models.PROTECT)
    vaqti = models.DateTimeField(default=timezone.now)
    adminReply = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)
    comment = models.TextField()
    def __str__(self):
        return str(self.user)
    
class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    maqola = models.ForeignKey('Maqola', on_delete=models.PROTECT)
    def __str__(self):
        return f'{self.user} - {self.maqola}'
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'maqola'],
                name='unique_like'
            )
        ]
class Category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name