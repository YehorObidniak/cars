# Generated by Django 4.1.7 on 2023-02-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_yallamotorcar_activelistings_yallamotorcar_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dubizzlecar',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
