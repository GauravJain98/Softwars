# Generated by Django 3.0 on 2019-12-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mainApp', '0015_auto_20191227_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]