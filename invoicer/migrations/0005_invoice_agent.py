# Generated by Django 5.0.2 on 2024-03-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicer', '0004_dailytotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='agent',
            field=models.CharField(default='Agent Name', max_length=100),
        ),
    ]
