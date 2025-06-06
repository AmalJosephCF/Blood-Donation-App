# Generated by Django 4.2.11 on 2024-05-06 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('patient_age', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=500)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('request_by_donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donor.donor')),
                ('request_by_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
