# Generated by Django 4.0.5 on 2022-06-28 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('website_updates', models.BooleanField(default=False)),
                ('recommended_researches', models.BooleanField(default=False)),
                ('active_trades', models.BooleanField(default=False)),
                ('send_update_emails', models.BooleanField(default=False)),
                ('newsletter', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
