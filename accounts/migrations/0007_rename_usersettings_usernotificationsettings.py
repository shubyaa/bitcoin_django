# Generated by Django 4.0.5 on 2022-06-28 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_usersettings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSettings',
            new_name='UserNotificationSettings',
        ),
    ]