# Generated by Django 5.0 on 2024-01-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_image_delete_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.FileField(upload_to='media/'),
        ),
    ]
