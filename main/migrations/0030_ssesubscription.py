# Generated by Django 4.1.7 on 2023-03-24 22:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_delete_ssesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSESubscription',
            fields=[
                ('ip_address', models.CharField(max_length=255)),
                ('connected_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('client_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
    ]
