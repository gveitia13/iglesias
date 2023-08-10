# Generated by Django 4.2.4 on 2023-08-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_distrito_cant_presbiterios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distrito',
            name='bautizados_espiritu',
            field=models.FloatField(blank=True, null=True, verbose_name='Bautizados Espíritu'),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='promedio_asistencia',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presbiterio',
            name='bautizados_espiritu',
            field=models.FloatField(blank=True, null=True, verbose_name='Bautizados Espíritu'),
        ),
        migrations.AlterField(
            model_name='presbiterio',
            name='promedio_asistencia',
            field=models.FloatField(blank=True, null=True),
        ),
    ]