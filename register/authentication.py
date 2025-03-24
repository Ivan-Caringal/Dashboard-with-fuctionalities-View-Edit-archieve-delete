from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import PermissionDenied  # Import exception
from .models import CustomUser

#backednd for modified authentication
class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None
        
        # Deny login if the approval status is pending or disapproved
        if user.approval_status == 'pending':
            raise PermissionDenied("Your account is pending approval.")
        elif user.approval_status == 'disapproved':
            raise PermissionDenied("Your account has been disapproved.")
        
        # Otherwise, allow normal authentication
        if user.check_password(password):
            return user
        return None
