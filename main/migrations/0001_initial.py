# Generated by Django 5.1.6 on 2025-03-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarangayFileReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('captain', models.CharField(max_length=255)),
                ('female_population', models.PositiveIntegerField(default=0)),
                ('male_population', models.PositiveIntegerField(default=0)),
                ('total_population', models.PositiveIntegerField(default=0)),
                ('age_0_5', models.PositiveIntegerField(default=0)),
                ('age_6_12', models.PositiveIntegerField(default=0)),
                ('age_13_17', models.PositiveIntegerField(default=0)),
                ('age_18_30', models.PositiveIntegerField(default=0)),
                ('age_31_45', models.PositiveIntegerField(default=0)),
                ('age_46_60', models.PositiveIntegerField(default=0)),
                ('age_60_plus', models.PositiveIntegerField(default=0)),
                ('pwd', models.PositiveIntegerField(default=0)),
                ('senior_assistance', models.PositiveIntegerField(default=0)),
                ('indigent', models.PositiveIntegerField(default=0)),
                ('total_pregnant', models.PositiveIntegerField(default=0)),
                ('high_risk_pregnant', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
