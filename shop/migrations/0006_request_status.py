# Generated by Django 4.2.2 on 2023-08-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('a', 'Accepted'), ('r', 'Refused')], default='', max_length=1),
        ),
    ]
