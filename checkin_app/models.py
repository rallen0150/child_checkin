from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



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
        return self.status == 'E'

    # @property
    # def all_time(self):
    #     return Time.objects.all()

    @property
    def payments(self):
        all_children = self.objects.all()
        total = sum(child.total_payment for child in all_children)
        return total

class Child(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    parent = models.ForeignKey('auth.User')
    pincode = models.CharField(max_length=4, unique=True)

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name

    @property
    def get_time(self):
        return Time.objects.filter(child=self)

    @property
    def full_time(self):
        get_time = self.get_time
        total = sum(time.daily_time.seconds for time in get_time)
        return round(total / 3600, 3)

    @property
    def total_payment(self):
        full_time = self.full_time
        hourly_rate = 300.00
        return round(float(full_time * hourly_rate), 2)


class Time(models.Model):
    child = models.ForeignKey(Child)
    checkin = models.BooleanField(default=False)
    checkin_time = models.DateTimeField(auto_now_add=True)
    checkout_time = models.DateTimeField(auto_now=True, null=True)

    @property
    def daily_time(self):
        return self.checkout_time - self.checkin_time
