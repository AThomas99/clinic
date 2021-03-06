# Generated by Django 3.2 on 2021-06-05 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_temperature', models.CharField(max_length=10)),
                ('body_pressure', models.CharField(max_length=10)),
                ('pulse_rate', models.CharField(max_length=10)),
                ('respiration_rate', models.CharField(max_length=10)),
                ('body_height', models.CharField(max_length=10)),
                ('body_weight', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Vitals',
                'ordering': ['-body_temperature'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
                ('telno', models.CharField(max_length=12)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('vitals', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.vital')),
            ],
            options={
                'verbose_name_plural': 'Patients',
                'ordering': ['-registered'],
            },
        ),
    ]
