# Generated by Django 4.1 on 2023-01-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VentaPost', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default='InstitutoZonaNorte/static/batman.png', upload_to=''),
        ),
    ]
