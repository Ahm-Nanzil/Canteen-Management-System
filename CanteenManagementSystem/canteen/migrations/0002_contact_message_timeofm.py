# Generated by Django 4.1.7 on 2023-04-24 09:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_message',
            name='timeofM',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]