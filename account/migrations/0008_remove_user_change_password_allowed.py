# Generated by Django 3.2.3 on 2021-10-19 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_change_password_allowed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='change_password_allowed',
        ),
    ]
