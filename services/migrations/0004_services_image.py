# Generated by Django 3.0.4 on 2020-03-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_remove_services_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.ImageField(default='a', upload_to='services', verbose_name='Image'),
        ),
    ]
