from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    contact = models.IntegerField()
    message = models.TextField()

    def get_absolute_url(self):
        return reverse('home:home-page')
