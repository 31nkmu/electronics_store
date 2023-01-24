# Generated by Django 4.1.5 on 2023-01-24 10:15

import creditcards.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('electronics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('order_confirm', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cc_number', creditcards.models.CardNumberField(max_length=25, verbose_name='card number')),
                ('cc_expiry', models.CharField(max_length=4)),
                ('cc_code', creditcards.models.SecurityCodeField(max_length=4, verbose_name='security code')),
                ('address', models.CharField(max_length=130)),
                ('confirm_code', models.CharField(blank=True, default='', max_length=130, null=True)),
                ('electronic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='electronics.electronic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
