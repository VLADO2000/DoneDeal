# Generated by Django 5.0.6 on 2024-06-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='label',
            field=models.CharField(default=None, max_length=255, verbose_name='brand name'),
        ),
    ]