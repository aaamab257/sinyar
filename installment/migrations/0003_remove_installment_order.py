# Generated by Django 4.2.2 on 2023-08-03 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('installment', '0002_installment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installment',
            name='order',
        ),
    ]
