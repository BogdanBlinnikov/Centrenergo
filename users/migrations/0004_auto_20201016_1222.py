# Generated by Django 3.1.2 on 2020-10-16 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201016_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='division_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.division'),
        ),
    ]
