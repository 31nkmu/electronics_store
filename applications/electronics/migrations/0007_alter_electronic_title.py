# Generated by Django 4.1.5 on 2023-01-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0006_alter_electronic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronic',
            name='title',
            field=models.TextField(),
        ),
    ]
