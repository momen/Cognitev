# Generated by Django 2.2.7 on 2019-12-07 00:18

import django.contrib.auth.models
from django.db import migrations, models
import model_utils.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('country_code', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('gender', model_utils.fields.StatusField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100, no_check_for_status=True)),
                ('birthdate', models.DateField()),
                ('avatar', models.ImageField(upload_to='uploads/')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
