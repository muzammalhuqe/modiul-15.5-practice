# Generated by Django 4.2.7 on 2023-12-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_instrument_remove_musician_instrument_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='instrument_type',
        ),
        migrations.AddField(
            model_name='musician',
            name='instrument_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Instrument',
        ),
    ]
