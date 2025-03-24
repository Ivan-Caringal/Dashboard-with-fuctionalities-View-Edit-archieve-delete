#here you create models for data base

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, default='Default Name')
    mobile = models.CharField(max_length=11, default='00000000000')
    barangay = models.CharField(max_length=100, default='barangay1')
    position = models.CharField(max_length=50, default='Secretary')
    barangayCode = models.CharField(max_length=10, default='0000000000')
    
    APPROVAL_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved')
    ]
    approval_status = models.CharField(
        max_length=11,
        choices=APPROVAL_CHOICES,
        default='pending'
    )

    # Add role field
    ROLE_CHOICES = [
    ('barangay-staff', 'Barangay Staff'),
    ('admin', 'Admin'),
    ('mddrmo-staff', 'MDDRMO Staff'),  # Added MDDRMO Staff
]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='barangay-staff'
    )

    def __str__(self):
        return self.username




# how can i add a button to send email?
# -can i add here a buttton for sending an email if approval_status has been change to approved?
#     https://www.youtube.com/watch?v=iGPPhzhXBFg

# in models.py
# @receiver(post_save, sender=CustomUser)
# def send_approval_email(sender, instance, **kwargs):
#     if instance.approval_status == "approved":  # Check if status is "approved"
#         subject = "Your Account Has Been Approved!"
#         message = f"Hello {instance.name},\n\nYour account has been approved. You can now log in.\n\nThank you!"
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [instance.email]  # Uses the user's email

#         send_mail(subject, message, from_email, recipient_list)

# in settings.py
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'  # Replace with your email
# EMAIL_HOST_PASSWORD = 'your-email-app-password'  # Use an app password, NOT your real password
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# in apps.py
# def ready(self):
#     import your_app_name.signals  # Replace with your actual app name

#     python manage.py makemigrations
# python manage.py migrate

