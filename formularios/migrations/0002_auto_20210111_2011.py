# Generated by Django 3.1.4 on 2021-01-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musico',
            name='banda',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='musico',
            name='pais',
            field=models.CharField(default='Chile', max_length=50),
        ),
    ]