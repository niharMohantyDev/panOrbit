# Generated by Django 4.2.1 on 2023-05-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccounts', '0005_alter_countrylanguage_is_official'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrylanguage',
            name='country_code',
            field=models.CharField(max_length=50),
        ),
    ]
