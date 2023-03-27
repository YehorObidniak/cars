# Generated by Django 4.1.7 on 2023-03-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_regspecs_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_any',
            old_name='price',
            new_name='currentPrice',
        ),
        migrations.AddField(
            model_name='car_any',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='car_any',
            name='oldPrice',
            field=models.IntegerField(null=True),
        ),
    ]