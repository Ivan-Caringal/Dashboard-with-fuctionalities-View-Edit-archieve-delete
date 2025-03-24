from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.
class BarangayDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)
    # name = models.CharField(max_length=255) if you want id dto accept duplicated barangay names
    captain = models.CharField(max_length=255)
    female_population = models.PositiveIntegerField(default=0)
    male_population = models.PositiveIntegerField(default=0)
    total_population = models.PositiveIntegerField(default=0)

    # Age Group Distribution
    age_0_5 = models.PositiveIntegerField(default=0)
    age_6_12 = models.PositiveIntegerField(default=0)
    age_13_17 = models.PositiveIntegerField(default=0)
    age_18_30 = models.PositiveIntegerField(default=0)
    age_31_45 = models.PositiveIntegerField(default=0)
    age_46_60 = models.PositiveIntegerField(default=0)
    age_60_plus = models.PositiveIntegerField(default=0)

    # Special Needs Categories
    pwd = models.PositiveIntegerField(default=0)
    senior_assistance = models.PositiveIntegerField(default=0)
    indigent = models.PositiveIntegerField(default=0)

    # Pregnancy Data
    total_pregnant = models.PositiveIntegerField(default=0)
    high_risk_pregnant = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Barangay Report - {self.name} (User: {self.user.username})"

    


class BarangayFileReport(models.Model):
    SEVERITY_CHOICES = [
        ("Informational", "Informational"),
        ("Minor", "Minor"),
        ("Major", "Major"),
        ("Critical", "Critical"),
    ]

    APPROVAL_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    resident_name = models.CharField(max_length=255)
    barangay_street = models.CharField(max_length=255)
    severity_level = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    incident_year = models.IntegerField()
    incident_month = models.CharField(max_length=20)
    incident_day = models.IntegerField()
    incident_time = models.TimeField()
    incident_type = models.TextField(blank=True, null=True)
    incident_description = models.TextField()
    attachments = models.FileField(upload_to='incident_attachments/', blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    approval_status = models.CharField(
        max_length=11,
        choices=APPROVAL_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)  # ✅ New field to track archived reports
    archived_at = models.DateTimeField(null=True, blank=True)  # Optional timestamp for when it was archived

    def archive(self):
        """ Archive this report instead of deleting it. """
        self.is_archived = True
        self.archived_at = timezone.now()
        self.save()

    def unarchive(self):
        """ Restore an archived report. """
        self.is_archived = False
        self.archived_at = None
        self.save()

    def __str__(self):
        status = "Archived" if self.is_archived else "Active"
        return f"{status}: {self.resident_name} - {self.incident_type} ({self.incident_year}-{self.incident_month}-{self.incident_day})"

