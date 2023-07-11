# Generated by Django 4.2.1 on 2023-05-21 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAccounts', '0002_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=52)),
                ('continent', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=26)),
                ('surface_area', models.FloatField()),
                ('indep_year', models.IntegerField(blank=True, null=True)),
                ('population', models.IntegerField()),
                ('life_expectancy', models.FloatField(blank=True, null=True)),
                ('gnp', models.FloatField(blank=True, null=True)),
                ('gnp_old', models.FloatField(blank=True, null=True)),
                ('local_name', models.CharField(max_length=45)),
                ('government_form', models.CharField(max_length=45)),
                ('head_of_state', models.CharField(blank=True, max_length=60, null=True)),
                ('capital', models.IntegerField(blank=True, null=True)),
                ('code2', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CountryLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('is_official', models.BooleanField()),
                ('percentage', models.FloatField()),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAccounts.country')),
            ],
        ),
    ]
