# Generated by Django 4.0.5 on 2022-06-28 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_usersettings_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserSettings',
        ),
    ]
