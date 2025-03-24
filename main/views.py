from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import BarangayDetails, BarangayFileReport
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.

def index(response):
    return render(response,"index.html")

def landing(response):
    return render(response,"landingpage.html")

@login_required(login_url='/loginBarangay')
def Barangaylandingpage(response):
    return render(response,"main/BarangayDashboard-LandingPage.html")

@login_required(login_url='/loginBarangay')
def BarangayDashboard(request):
    reportLogDashboards = BarangayFileReport.objects.filter(user=request.user, is_archived=False)
    barangaydetailsLogDashboards = BarangayDetails.objects.filter(user=request.user).order_by('-id').first() 
    
    print(barangaydetailsLogDashboards.male_population, barangaydetailsLogDashboards.female_population)

    data = {
        'reportLogDashboards': reportLogDashboards,
        'barangaydetailsLogDashboards': barangaydetailsLogDashboards,
    } 
    return render(request,"main/BarangayDashboard-Dashboard.html", data)

# for update button
# @login_required(login_url='/loginBarangay')
# def BarangayReportLog(request):
#     reportsLogs = BarangayFileReport.objects.filter(user=request.user)
    
#     if request.method == "POST":
#         report_id = request.POST.get("report_id")
#         new_status = request.POST.get("approval_status")

#         print(f"Received Data - Report ID: {report_id}, New Status: {new_status}")  

#         try:
#             report = BarangayFileReport.objects.get(id=report_id)
#             report.approval_status = new_status
#             report.save()
#             print("✅ Update Successful!")  
#         except BarangayFileReport.DoesNotExist:
#             print("❌ Report not found!")  
            

#     data = {
#         'reportsLogs': reportsLogs,
#     } 

#     return render(request, "main/BarangayDashboard-ReportLog.html", data)



@login_required(login_url='/loginBarangay')

def BarangayReportLog(request):
    reportsLogs = BarangayFileReport.objects.filter(user=request.user, is_archived=False)

    if request.method == "POST":
        archive_id = request.POST.get("archive_id", "").strip()  # ✅ Ensure it's not empty
        delete_id = request.POST.get("delete_id", "").strip()  # ✅ Ensure it's not empty
        report_id = request.POST.get("report_id", "").strip()  # ✅ Ensure it's not empty

        # 🟢 Archive Report
        if archive_id:
            try:
                report = get_object_or_404(BarangayFileReport, id=int(archive_id), user=request.user)
                report.archive()  # Calls the `archive()` method
                messages.success(request, "Report archived successfully!")
            except (BarangayFileReport.DoesNotExist, ValueError):
                messages.error(request, "Report not found or invalid ID!")

            return redirect("BarangayReportLog")

        # 🗑️ Delete Report
        if delete_id:
            try:
                report = get_object_or_404(BarangayFileReport, id=int(delete_id), user=request.user)
                report.delete()
                messages.success(request, "Report deleted successfully!")
            except (BarangayFileReport.DoesNotExist, ValueError):
                messages.error(request, "Report not found or invalid ID!")

            return redirect("BarangayReportLog")

        # 🟢 Handle Edit/Update Request
        if report_id:
            try:
                report = get_object_or_404(BarangayFileReport, id=int(report_id), user=request.user)

                new_date = request.POST.get("date", "").strip()
                new_time = request.POST.get("time", "").strip()
                new_severity = request.POST.get("severity", "").strip()
                new_incident = request.POST.get("incident", "").strip()
                new_status = request.POST.get("approval_status", "").strip()

                # 🟢 Update Date
                if new_date:
                    try:
                        date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                        report.incident_year = date_obj.year
                        report.incident_month = date_obj.strftime("%B")
                        report.incident_day = date_obj.day
                    except ValueError:
                        messages.error(request, "Invalid Date Format")

                # 🔵 Update Time
                if new_time:
                    try:
                        time_obj = datetime.datetime.strptime(new_time, "%H:%M").time()
                        report.incident_time = time_obj
                    except ValueError:
                        messages.error(request, "Invalid Time Format")

                # Update Other Fields
                if new_severity:
                    report.severity_level = new_severity
                if new_incident:
                    report.incident_type = new_incident
                if new_status:
                    report.approval_status = new_status

                report.save()
                messages.success(request, "Report updated successfully!")

            except (BarangayFileReport.DoesNotExist, ValueError):
                messages.error(request, "Report not found or invalid ID!")

    data = {"reportsLogs": reportsLogs}
    return render(request, "main/BarangayDashboard-ReportLog.html", data)




@login_required(login_url='/loginBarangay')
def barangay_details_view(request):
    print("Function called")  # Debugging
    if request.method == 'POST':
        print("Form submitted!")  # Debugging

        # Get data from the form
        brgy_name = request.POST.get('brgyName')
        brgy_captain = request.POST.get('brgyCaptain')
        female_population = request.POST.get('femalePopulation')
        male_population = request.POST.get('malePopulation')
        total_population = request.POST.get('populationTotal')

        age_0_5 = request.POST.get('age0-5')
        age_6_12 = request.POST.get('age6-12')
        age_13_17 = request.POST.get('age13-17')
        age_18_30 = request.POST.get('age18-30')
        age_31_45 = request.POST.get('age31-45')
        age_46_60 = request.POST.get('age46-60')
        age_60_plus = request.POST.get('age60plus')

        pwd = request.POST.get('pwd')
        senior_assistance = request.POST.get('seniorAssistance')
        indigent = request.POST.get('indigent')

        total_pregnant = request.POST.get('totalPregnant')
        high_risk_pregnant = request.POST.get('highRiskPregnant')

        # Convert numeric fields to integers (to avoid errors)
        female_population = int(female_population) if female_population else 0
        male_population = int(male_population) if male_population else 0
        total_population = int(total_population) if total_population else 0

        # Store data in the database
        barangay = BarangayDetails.objects.create(
            user=request.user,  # Associate the logged-in user
            name=brgy_name,
            captain=brgy_captain,
            female_population=female_population,
            male_population=male_population,
            total_population=total_population,
            age_0_5=int(age_0_5) if age_0_5 else 0,
            age_6_12=int(age_6_12) if age_6_12 else 0,
            age_13_17=int(age_13_17) if age_13_17 else 0,
            age_18_30=int(age_18_30) if age_18_30 else 0,
            age_31_45=int(age_31_45) if age_31_45 else 0,
            age_46_60=int(age_46_60) if age_46_60 else 0,
            age_60_plus=int(age_60_plus) if age_60_plus else 0,
            pwd=int(pwd) if pwd else 0,
            senior_assistance=int(senior_assistance) if senior_assistance else 0,
            indigent=int(indigent) if indigent else 0,
            total_pregnant=int(total_pregnant) if total_pregnant else 0,
            high_risk_pregnant=int(high_risk_pregnant) if high_risk_pregnant else 0,
        )

        return redirect('/barangay_details_view')  # Redirect to a barangay list page or another view

    return render(request, 'main/BarangayDashboard-BarangayDetails.html')  # Render your form template

@login_required(login_url='/loginBarangay')
def barangay_file_report_view(request):
    if request.method == 'POST':
        # Debugging
        print("Form Submitted!")

        # Get form data
        resident_name = request.POST.get('residentName')
        barangay_street = request.POST.get('barangayStreet')
        severity_level = request.POST.get('severityLevel')
        incident_year = request.POST.get('incidentYear')
        incident_month = request.POST.get('incidentMonth')
        incident_day = request.POST.get('incidentDay')
        incident_time = request.POST.get('incidentTime')
        incident_type = request.POST.get('incidentType')
        incident_description = request.POST.get('incidentDescription')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        approval_status = 'pending'  # Default value

        # Handle file upload
        attachments = request.FILES.get('attachments')

        # Convert numerical fields
        incident_year = int(incident_year) if incident_year else None
        incident_day = int(incident_day) if incident_day else None
        latitude = float(latitude) if latitude else None
        longitude = float(longitude) if longitude else None

        # Save data to database
        report = BarangayFileReport.objects.create(
            user=request.user,  # Associate the logged-in user
            resident_name=resident_name,
            barangay_street=barangay_street,
            severity_level=severity_level,
            incident_year=incident_year,
            incident_month=incident_month,
            incident_day=incident_day,
            incident_time=incident_time,
            incident_type=incident_type,
            incident_description=incident_description,
            attachments=attachments,
            latitude=latitude,
            longitude=longitude,
            approval_status=approval_status,
        )

        return redirect('/barangay_file_report_view')  # Redirect to a list page or success page

    return render(request, 'main/BarangayDashboard-FileReport.html')  # Render the form page

