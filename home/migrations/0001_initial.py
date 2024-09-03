# Generated by Django 3.0 on 2022-09-26 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(default=None, max_length=30)),
                ('mob', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('edt', models.DateField()),
                ('remarks', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=20)),
                ('languages', models.CharField(max_length=30)),
                ('sal', models.IntegerField()),
                ('joined_dt', models.DateField()),
                ('timinings', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Joined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_dt', models.DateField()),
                ('total', models.IntegerField()),
                ('first_ins', models.IntegerField()),
                ('first_dt', models.DateField()),
                ('second_ins', models.IntegerField()),
                ('second_dt', models.DateField()),
                ('duration', models.CharField(max_length=20)),
                ('dues', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_dt', models.DateField()),
                ('trainer', models.CharField(max_length=20)),
                ('bname', models.CharField(max_length=30)),
                ('student', models.ManyToManyField(to='home.Joined')),
            ],
        ),
    ]