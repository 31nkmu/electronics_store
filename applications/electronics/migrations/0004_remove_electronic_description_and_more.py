# Generated by Django 4.1.5 on 2023-01-20 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0003_alter_image_electronic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electronic',
            name='description',
        ),
        migrations.RemoveField(
            model_name='electronic',
            name='category',
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thickness', models.CharField(blank=True, max_length=128, null=True)),
                ('display', models.CharField(blank=True, max_length=128, null=True)),
                ('processor', models.CharField(blank=True, max_length=128, null=True)),
                ('video', models.CharField(blank=True, max_length=10, null=True)),
                ('memory', models.CharField(blank=True, max_length=120, null=True)),
                ('size', models.CharField(blank=True, max_length=128, null=True)),
                ('weight', models.CharField(blank=True, max_length=128, null=True)),
                ('electronic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='electronics', to='electronics.electronic')),
            ],
        ),
        migrations.AddField(
            model_name='electronic',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='electronics', to='electronics.category'),
            preserve_default=False,
        ),
    ]