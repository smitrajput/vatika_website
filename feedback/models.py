from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
# Create your models here.
class Feedback(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    review_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    drop_a_note = models.TextField(blank=True)
    suggest_menu_item = models.CharField(max_length=25, blank=True)

    def get_absolute_url(self):
        return reverse('home:home-page')
