# Generated by Django 3.1 on 2020-09-20 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0038_auto_20200827_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsable_difunto',
            name='correo',
            field=models.EmailField(blank=True, default=None, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='responsable_difunto',
            name='direccion',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
