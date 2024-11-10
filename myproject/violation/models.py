from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Violation(models.Model):
    VIOLATION_TYPES = [
        ('Without Shoes', 'Without Shoes'),
        ('Without Helmet', 'Without Helmet'),
        ('Both', 'Both')  
    ]

    created_at = models.DateTimeField(default=timezone.now)  
    violation_type = models.CharField(max_length=20, choices=VIOLATION_TYPES)
    camera_number = models.IntegerField()  
    image = models.ImageField(upload_to='uploaded_images/images', blank=True, null=True)  # Image field, nullable
    without_jacket = models.BooleanField(default=False) 
    without_helmet = models.BooleanField(default=False)
    both = models.BooleanField(default=False) 
    def clean(self):
        
        if self.camera_number <= 0:
            raise ValidationError("Camera number must be a positive integer.")

    def __str__(self):
        return f"{self.violation_type} - Camera {self.camera_number} on {self.created_at}"

    class Meta:
        verbose_name = "Violation"
        verbose_name_plural = "Violations"
        ordering = ['camera_number']
