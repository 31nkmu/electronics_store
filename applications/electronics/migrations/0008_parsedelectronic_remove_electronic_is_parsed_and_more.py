# Generated by Django 4.1.5 on 2023-01-21 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electronics', '0007_alter_electronic_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedElectronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='electronic',
            name='is_parsed',
        ),
        migrations.AlterField(
            model_name='electronic',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='electronics', to='electronics.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='electronic',
            name='title',
            field=models.CharField(max_length=88),
        ),
        migrations.AlterField(
            model_name='electronic',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='electronics', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recommendimages',
            name='electronic_recommend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='electronics.parsedelectronic'),
        ),
    ]