# Generated by Django 4.2.2 on 2023-09-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_adminnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminnotification',
            name='title',
            field=models.CharField(default='', max_length=55),
        ),
    ]
