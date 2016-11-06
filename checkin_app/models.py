from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Child(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    parent = models.ForeignKey('auth.User')
    pincode = models.CharField(max_length=4, unique=True)
    picture = models.FileField(null=True, blank=True)

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name

    @property
    def get_time(self):
        return Time.objects.filter(child=self)

    @property
    def total_payment(self):
        get_time = self.get_time
        total = round(sum(time.daily_time.seconds for time in get_time)/3600, 3)
        hourly_rate = 300.00
        return round(float(total * hourly_rate), 2)

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "https://secure.gravatar.com/avatar/ad516503a11cd5ca435acc9bb6523536?s=1024&d=mm&r=g"


class Time(models.Model):
    child = models.ForeignKey(Child)
    checkin = models.BooleanField(default=False)
    checkin_time = models.DateTimeField(auto_now_add=True)
    checkout_time = models.DateTimeField(auto_now=False, null=True)

    @property
    def daily_time(self):
        return self.checkout_time - self.checkin_time


ACCESS_LEVEL = [
    ('P', 'Parent'),
    ('E', 'Employee')
]

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance, access_level='P')


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVEL)

    @property
    def is_employee(self):
        return self.access_level == 'E'
