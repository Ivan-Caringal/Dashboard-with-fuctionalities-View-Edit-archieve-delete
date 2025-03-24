# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from django.contrib.auth import authenticate, get_user_model


#here you create create custom forms

#custom form for barangay-staff
User = get_user_model()

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }),
        help_text="Enter your registered username."
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        help_text="Your password is case-sensitive."
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Fetch user object
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError('Invalid username or password.')

        # Check approval status before authentication
        if user.approval_status == 'pending':
            raise ValidationError('Your account is pending approval.')
        elif user.approval_status == 'disapproved':
            raise ValidationError('Your account has been disapproved.')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Invalid username or password.')

        # Role validation: Only allow 'barangay-staff' to log in
        if user.role != 'barangay-staff':
            raise ValidationError('Only Barangay Staff are allowed to log in.')

        # Save the authenticated user in cleaned_data
        cleaned_data['user'] = user
        return cleaned_data
    
#custom form for MDRRMO-staff
class CustomAuthenticationFormMdrrmo(forms.Form):
    username = forms.CharField(
        max_length=150, 
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }),
        help_text="Enter your registered username."
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        help_text="Your password is case-sensitive."
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Fetch user object
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError('Invalid username or password.')

        # Check approval status before authentication
        if user.approval_status == 'pending':
            raise ValidationError('Your account is pending approval.')
        elif user.approval_status == 'disapproved':
            raise ValidationError('Your account has been disapproved.')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Invalid username or password.')

        # Role validation: Only allow 'barangay-staff' to log in
        if user.role != 'mddrmo-staff':
            raise ValidationError('Only MDRRMO Staff are allowed to log in.')

        # Save the authenticated user in cleaned_data
        cleaned_data['user'] = user
        return cleaned_data

#custom form REGISTER

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150, required=True, label="Username",
        help_text="Enter your username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a unique username',
        })
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a strong password',
        }),
        help_text="Your password must be at least 8 characters long and not entirely numeric."
    )

    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter your password',
        }),
        help_text="Enter the same password for verification."
    )

    name = forms.CharField(
        max_length=100, required=True, label="Name",
        help_text="Enter your full name.",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name'
        })
    )

    email = forms.EmailField(
        required=True, label="Email",
        help_text="Enter your email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a valid email address.'
        })
    )
    

    mobile = forms.RegexField(
        regex=r'^09[0-9]{9}$',
        required=True,
        label="Mobile Number",
        help_text="Enter your mobile number .",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'mobile',
            'type': 'tel',  
            'placeholder': 'Enter your mobile number (ex. 09xxxxxxxxx)',
            'pattern': '^09[0-9]{9}$',
            'inputmode': 'numeric',
            'required': True
        })
    )

    barangay = forms.ChoiceField(
        choices=[
            ('', 'Select your barangay'),
            ('barangay1', 'Barangay 1'),
            ('barangay2', 'Barangay 2'),
            ('barangay3', 'Barangay 3')
        ],
        required=True, label="Barangay",
        help_text="Select your barangay from the list.",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    position = forms.ChoiceField(
        choices=[
            ('', 'Select your position'),
            ('chairman', 'Chairman'),
            ('kagawad', 'Kagawad'),
            ('secretary', 'Secretary'),
            ('treasurer', 'Treasurer')
        ],
        required=True, label="Position",
        help_text="Select your official position.",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    barangayCode = forms.RegexField(
        regex=r'^\d{10}$',  # Ensures exactly 10 digits (no letters or special characters)
        required=True,
        label="Barangay Code",
        help_text="Enter your 10-digit barangay code.",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'barangayCode',
            'type': 'text',  
            'placeholder': 'Enter 10-digit barangay code',
            'pattern': '^[0-9]{10}$',  # Matches the regex requirement
            'inputmode': 'numeric',
            'required': True
        })
    )

    class Meta:
        model = CustomUser
        fields = ["username", "name", "email", "mobile", "barangay", "position", "barangayCode", "password1", "password2"]








User = get_user_model()

class CustomAdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }),
        help_text="Enter your registered username."
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        help_text="Your password is case-sensitive."
    )

    error_messages = {
        'invalid_login': "Invalid username or password.",
        'inactive': "This account is inactive. Please contact support.",
        'role_not_allowed': "Only Admin users are allowed to log in."
    }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise ValidationError(self.error_messages['invalid_login'], code='invalid_login')
            elif not user.is_active:
                raise ValidationError(self.error_messages['inactive'], code='inactive')
            elif user.role != 'admin':  # ✅ Check if user is an Admin
                raise ValidationError(self.error_messages['role_not_allowed'], code='role_not_allowed')

        return cleaned_data