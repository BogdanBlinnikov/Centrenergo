# Generated by Django 3.1.2 on 2020-10-18 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201016_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='depart',
            field=models.CharField(max_length=100, null=True, verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='division',
            name='depart_div',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.department', verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='division',
            name='div',
            field=models.CharField(max_length=100, null=True, verbose_name='Відділ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='День народження'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.department', verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='user',
            name='division_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.division', verbose_name='Відділ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_dir',
            field=models.BooleanField(default=False, verbose_name='Директор'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(max_length=50, null=True, verbose_name='По-батькові'),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(max_length=100, null=True, verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='user',
            name='short_tel_number',
            field=models.CharField(max_length=5, null=True, verbose_name='Короткий тел. номер'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel_number',
            field=models.CharField(max_length=14, null=True, verbose_name='Тел. номер'),
        ),
    ]
