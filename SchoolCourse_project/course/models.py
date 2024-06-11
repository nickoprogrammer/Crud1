from django.db import models
from django.utils import timezone

class Course(models.Model):
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('pending', 'Pending'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
