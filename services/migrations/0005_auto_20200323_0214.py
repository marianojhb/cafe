# Generated by Django 3.0.4 on 2020-03-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_services_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
