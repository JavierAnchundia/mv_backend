# Generated by Django 3.1 on 2020-08-23 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0013_merge_20200822_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camposanto',
            name='id_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='serviciosBackend.empresa'),
        ),
    ]
