# Generated by Django 5.0.2 on 2024-02-26 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdata',
            name='temp',
            field=models.CharField(max_length=20),
        ),
    ]
