from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Child(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    checkin_time = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('auth.User')
    checkin = models.BooleanField(default=False)
    checkout_time = models.DateTimeField(auto_now=True)
    onsite = models.BooleanField(default=False)

class Pin(models.Model):
    child = models.OneToOneField(Child)
    pin_number = models.IntegerField()

# class Daycare(models.Model):
#     daycare = models.ManyToManyField(Child)

STATUS = {
    ('O', 'Owner'),
    ('P', 'Parent')
}

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    status = models.CharField(max_length=1, choices=STATUS)

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance, status='P')
