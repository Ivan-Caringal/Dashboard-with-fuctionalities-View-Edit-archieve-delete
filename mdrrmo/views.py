from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main.models import BarangayDetails, BarangayFileReport
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
def mdrrmolandingpage(response):
    return render(response,"mdrrmo/mdrrmo_landingpage.html")

def cms(response):
    return render(response,"mdrrmo/mdrrmo_cms.html")

def report(response):
    reportLogStaffs = BarangayFileReport.objects.all()
    data = {
        'reportLogStaffs': reportLogStaffs,
    } 
    return render(response,"mdrrmo/mdrrmo_report.html",data)



def report_detail(request, id):
    single_report = get_object_or_404(BarangayFileReport, pk=id)

    if request.method == "POST":
        action = request.POST.get("action")  # Get the action (approve/disapprove)

        if action == "approve":
            single_report.approval_status = "approved"  # Change to lowercase
        elif action == "disapprove":
            single_report.approval_status = "disapproved"  # Change to lowercase

        single_report.save()  # Save the updated status in the database

        return redirect("report_detail", id=id)  # Reload the page after updating

    data = {
        'single_report': single_report,
    }
    return render(request, "mdrrmo/reportDetail.html", data)

   


