# Generated by Django 4.1.5 on 2023-01-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0009_alter_recommendimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendimages',
            name='image',
            field=models.TextField(),
        ),
    ]
