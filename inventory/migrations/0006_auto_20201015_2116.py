# Generated by Django 3.1.2 on 2020-10-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20201015_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicechars',
            name='clock_frequency',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='devicechars',
            name='diagonal',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='devicechars',
            name='ram_size',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
