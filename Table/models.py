from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

def validate_even(value):
    if value > 4:
        raise ValidationError(
            _('%(value)s should not be greater than 4'),
            params={'value': value},
        )

class BookTable(models.Model):
    booked_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='booktables')
    customer = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    total_persons = models.IntegerField(validators=[validate_even])
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.customer



    def get_absolute_url(self):
        return reverse('Table:confirm-mail')


class BookLawn(models.Model):
    booked_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='booklawns')
    customer = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    total_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.customer

    def get_absolute_url(self):
        return reverse('home:home-page')
