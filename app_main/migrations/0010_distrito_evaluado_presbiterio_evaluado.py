# Generated by Django 4.2.4 on 2023-09-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0009_alter_resumendistrito_cantidad_meses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='distrito',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='presbiterio',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
    ]
