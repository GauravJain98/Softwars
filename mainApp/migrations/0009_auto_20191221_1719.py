# Generated by Django 3.0 on 2019-12-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_auto_20191221_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemstatement',
            name='organization',
            field=models.CharField(max_length=200),
        ),
    ]