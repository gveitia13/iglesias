# Generated by Django 4.2.4 on 2023-08-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('1', 'Jefe de Distro'), ('2', 'Jefe de Presbiterio')], default='2', max_length=2, verbose_name='Rol'),
        ),
    ]