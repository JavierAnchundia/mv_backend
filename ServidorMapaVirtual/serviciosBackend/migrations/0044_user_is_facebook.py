# Generated by Django 3.1 on 2020-10-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0043_auto_20200929_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_facebook',
            field=models.BooleanField(default=False),
        ),
    ]
