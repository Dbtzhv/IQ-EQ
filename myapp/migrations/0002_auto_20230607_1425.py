# Generated by Django 3.2 on 2023-06-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eqtestresult',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='iqtestresult',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
