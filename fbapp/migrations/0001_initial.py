# Generated by Django 2.2.7 on 2019-11-14 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=25)),
                ('fk_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbapp.Login')),
            ],
        ),
    ]
