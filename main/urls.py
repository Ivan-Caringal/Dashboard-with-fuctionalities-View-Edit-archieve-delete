from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns= [
path("", views.landing, name="landing"),
path("home/", views.index, name="index"),
path('login/', LoginView.as_view(template_name='register/templates/BarangayLogin.html'), name='login'),
path("Barangaylandingpage/", views.Barangaylandingpage, name="Barangaylandingpage"),
path("barangay_details_view/", views.barangay_details_view, name="BarangayDetails"),
path("BarangayDashboard/", views.BarangayDashboard, name="BarangayDashboard"),
path("barangay_file_report_view/", views.barangay_file_report_view, name="BarangayFileReport"),
path("BarangayReportLog/", views.BarangayReportLog, name="BarangayReportLog"),



]