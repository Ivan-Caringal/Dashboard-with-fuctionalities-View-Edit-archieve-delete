from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='BarangayLogin.html'), name='login'),
    # other URL patterns related to registration, etc.
    # For example:
    # path('register/', views.register, name='register'),
]
