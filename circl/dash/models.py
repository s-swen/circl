# models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('friend', 'Friend'),
        ('professional', 'Professional'),
        ('doctor', 'Doctor'),
        ('lawyer', 'Lawyer'),
        ('relative', 'Relative'),
        ('schoolmate', 'Schoolmate'),
        ('love_interest', 'Love Interest'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    last_contact = models.DateField(blank=True, null=True)
    work = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    instagram_handle = models.CharField(max_length=100, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='friend'
    )
    custom_category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    uploaded_document = models.FileField(upload_to='documents/', blank=True, null=True)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_category(self):
        if self.custom_category:
            return self.custom_category.name
        return self.get_category_display()

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])