# Generated by Django 3.2 on 2023-06-07 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IQTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.test')),
            ],
        ),
        migrations.CreateModel(
            name='EQTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letters', models.CharField(max_length=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.test')),
            ],
        ),
    ]
