# Generated by Django 4.0.6 on 2022-07-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('receiver', models.CharField(max_length=100, null=True)),
                ('datetrans', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('accno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('accbal', models.IntegerField()),
            ],
        ),
    ]