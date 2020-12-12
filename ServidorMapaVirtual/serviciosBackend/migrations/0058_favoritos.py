<<<<<<< HEAD
# Generated by Django 3.1 on 2020-11-16 09:04
=======
# Generated by Django 3.1 on 2020-11-14 20:37
>>>>>>> 158944e4f9d5dd7d40643e614c691e74f70ae990

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosBackend', '0057_tokendevice_plataform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id_favorito', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('estado', models.BooleanField(default=False)),
                ('id_difunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviciosBackend.difunto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
