# Generated by Django 3.0.8 on 2020-07-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_auto_20200711_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='aid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
