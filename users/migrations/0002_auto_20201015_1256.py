# Generated by Django 3.1.2 on 2020-10-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_dir',
            field=models.BooleanField(default=False),
        ),
    ]
