# Generated by Django 4.1.7 on 2023-03-09 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_regspecs_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regspecs',
            name='site',
        ),
    ]
