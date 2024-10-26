# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for the profile

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('family', 'Family'),
        ('alumni', 'Alumni'),
        ('other', 'Other'), 
    ]

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"