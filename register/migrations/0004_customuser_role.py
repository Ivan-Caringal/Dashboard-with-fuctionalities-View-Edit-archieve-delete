# Generated by Django 5.1.6 on 2025-02-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_customuser_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('barangay-staff', 'Barangay Staff'), ('admin', 'Admin')], default='barangay-staff', max_length=20),
        ),
    ]
