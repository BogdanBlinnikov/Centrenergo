# Generated by Django 3.1.2 on 2020-10-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201016_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
