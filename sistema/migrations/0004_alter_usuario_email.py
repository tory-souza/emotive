# Generated by Django 5.1.1 on 2024-11-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_remove_usuario_tipousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
