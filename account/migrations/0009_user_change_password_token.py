# Generated by Django 3.2.3 on 2021-10-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_user_change_password_allowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='change_password_token',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
