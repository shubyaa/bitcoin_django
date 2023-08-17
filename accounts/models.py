from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import BooleanField


# Create your models here.

# Adding Custom fields to the existing auth_user table of django

class UserModel(AbstractUser):
    email_verification = models.BooleanField(default=False)


# User Settings Model
class UserNotificationSettings(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)

    user_id = models.ForeignKey(UserModel, on_delete=models.PROTECT)

    # Settings regrding trades
    website_updates = models.BooleanField(default=False)
    recommended_researches = models.BooleanField(default=False)
    active_trades = models.BooleanField(default=False)

    # Settings regarding Email Notifications
    send_update_emails = models.BooleanField(default=False)  
    newsletter = models.BooleanField(default=False)

    # Privacy Settings
    show_on_search = models.BooleanField(default=True)

 

