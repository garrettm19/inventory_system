# Generated by Django 4.2.1 on 2023-05-16 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('ssn_number', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('rank', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('serial_number', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('si_type', models.CharField(max_length=255)),
                ('weapon_status', models.BooleanField(default=False)),
                ('user_ssn_number', models.ForeignKey(db_column='user_ssn_number', on_delete=django.db.models.deletion.CASCADE, related_name='weapons', to='myapp.user')),
            ],
            options={
                'db_table': 'weapons',
            },
        ),
    ]
