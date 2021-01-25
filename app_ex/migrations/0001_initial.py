# Generated by Django 3.1.5 on 2021-01-25 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('altura', models.DecimalField(decimal_places=1, max_digits=4)),
                ('peso', models.DecimalField(decimal_places=1, max_digits=4)),
                ('direccion', models.CharField(max_length=300)),
                ('codigo_postal', models.CharField(max_length=20)),
                ('archivo_foto', models.CharField(default='sin asignar', max_length=400)),
                ('rol', models.CharField(default='sin asignar', max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
