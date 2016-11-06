from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Child(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # checkin_time = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('auth.User')
    parent = models.ForeignKey('checkin_app.Profile')
    # checkout_time = models.DateTimeField(auto_now=True)
    pin_number = models.CharField(max_length=4, unique=True)
    # checkin = models.BooleanField(default=False)

    @property
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name

    @property
    def get_time(self):
        return Time.objects.get(child=self)

# class Pin(models.Model):
#     child = models.OneToOneField(Child)
#     pin_number = models.IntegerField()


class Time(models.Model):
    checkin_time = models.DateTimeField(auto_now_add=True)
    checkout_time = models.DateTimeField(auto_now=False, null=True)
    child = models.ForeignKey(Child)
    checkin = models.BooleanField(default=False)



STATUS = [
    ('O', 'Owner'),
    ('P', 'Parent')
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance, status='P')
