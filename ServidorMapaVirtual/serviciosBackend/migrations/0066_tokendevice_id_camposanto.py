# Generated by Django 3.1 on 2020-12-16 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0065_auto_20201212_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokendevice',
            name='id_camposanto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serviciosBackend.camposanto'),
        ),
    ]
