# Generated by Django 3.1 on 2020-12-12 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0063_notificaciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificaciones',
            old_name='descripcion',
            new_name='mensaje',
        ),
        migrations.RenameField(
            model_name='notificaciones',
            old_name='nombre',
            new_name='titulo',
        ),
    ]