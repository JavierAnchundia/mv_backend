# Generated by Django 3.1 on 2021-01-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0067_auto_20201229_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Sugerencia', 'verbose_name_plural': 'Sugerencias'},
        ),
        migrations.AddField(
            model_name='notificaciones',
            name='tipo',
            field=models.CharField(choices=[('paquete', 'paquete'), ('tip', 'tip')], default='tip', max_length=40),
        ),
    ]
