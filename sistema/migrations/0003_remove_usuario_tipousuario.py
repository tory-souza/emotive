# Generated by Django 5.1.3 on 2024-11-29 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_usuario_remove_diario_keymedico_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tipoUsuario',
        ),
    ]
