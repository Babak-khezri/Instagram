# Generated by Django 3.2 on 2021-04-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='chat/files')),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='files',
        ),
    ]