# Generated by Django 4.2.2 on 2023-08-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installment', '0005_alter_installment_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='installment',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='start_date',
            field=models.DateField(),
        ),
    ]
