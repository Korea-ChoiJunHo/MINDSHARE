# Generated by Django 2.2.3 on 2019-08-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_app', '0005_library_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile1',
            name='birth_date',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
