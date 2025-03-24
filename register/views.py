from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from .forms import RegisterForm
from .forms import CustomAuthenticationForm
from .forms import CustomAdminLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomAuthenticationFormMdrrmo



#here you manage the action the the user do and manage what to show to them from that specific action
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            print("Account saved")
            return redirect("/")
        else:
            print("Form is not valid")
            return render(response, 'Registrationform.html', {'form': form})
    else:
        form = RegisterForm()
        print("GET request - displaying empty form")
    return render(response, 'Registrationform.html', {'form': form})



def barangay_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)  # ✅ Removed `request` argument
        if form.is_valid():
            user = form.cleaned_data.get('user')  # ✅ Correct way to retrieve the authenticated user
            login(request, user) 
            return redirect('/Barangaylandingpage')  # Default redirection
        # Handle errors properly
        for field_errors in form.errors.values():
            for error in field_errors:
                messages.error(request, error)

        return redirect('/loginBarangay')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'BarangayLogin.html', {'form': form})



def mddrmostaff_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationFormMdrrmo(data=request.POST)  # ✅ Removed `request` argument
        if form.is_valid():
            user = form.cleaned_data.get('user')  # ✅ Correct way to retrieve the authenticated user
            login(request, user) 
            return redirect('/mddrmo/mdrrmolandingpage/')  # Default redirection
        # Handle errors properly
        for field_errors in form.errors.values():
            for error in field_errors:
                messages.error(request, error)

        return redirect('/loginMddrmo')
    else:
        form = CustomAuthenticationFormMdrrmo()

    return render(request, 'MddrmoStaffLogin.html', {'form': form})




class CustomAdminLoginView(LoginView):
    authentication_form = CustomAdminLoginForm
    template_name = 'admin/login.html'  # Ensure this exists in templates/admin/

    def get_success_url(self):
        return reverse_lazy('admin:index')  # Redirect to Django Admin dashboard
    
