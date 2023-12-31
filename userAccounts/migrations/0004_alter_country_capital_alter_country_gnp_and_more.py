# Generated by Django 4.2.1 on 2023-05-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccounts', '0003_country_countrylanguage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='gnp',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='gnp_old',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='indep_year',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='life_expectancy',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='surface_area',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='countrylanguage',
            name='percentage',
            field=models.CharField(),
        ),
    ]
