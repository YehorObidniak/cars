# Generated by Django 4.1.7 on 2023-06-13 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_car_any_test_alter_car_any_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_any',
            name='photo',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='car_any',
            name='post_created_at',
            field=models.IntegerField(default=1686692528.8723183),
        ),
    ]
