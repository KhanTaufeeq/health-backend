# Generated by Django 5.1.4 on 2025-01-15 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diabetes',
            old_name='fastin_sugar',
            new_name='fasting_sugar',
        ),
    ]