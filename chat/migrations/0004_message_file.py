# Generated by Django 3.2 on 2021-04-22 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210422_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.filemessage'),
        ),
    ]
