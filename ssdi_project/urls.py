"""ssdi_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from views import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^register/', signup_page, name="signup"),
    url(r'^login/', login_page, name="login"),
    url(r'^logout/', logout_user, name="logout"),
    url(r'^doctors/', show_doctors, name="ShowDoctors"),
    url(r'^success/(\w+)/(\w+)', login_successful, name="success"),
    url(r'^timings/(\w+)/(\w+)', set_office_hours, name="OfficeHours"),
    url(r'^beds/(\w+)/', check_beds, name="CheckBeds"),
    url(r'^admit/(\w+)/', admit_patient, name="admitPatient"),
    url(r'^discharge/(\w+)/', discharge_patient, name="dischargePatient"),
    url(r'^generateBill/(\w+)/', generate_bill, name="generateBill"),
    url(r'^doctoradd/(\w+)/', doctor_add, name="doctoradd"),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^testdb/', test_database, name="testdb"),
    url(r'^backenddb/', backend_adder, name="BackEndAdder"),
    url(r'^viewtimings/(\w+)/', view_time, name="SpecificDoctorTime"),
    url(r'^book/(\w+)/', book_appointment, name="BookAppointment"),
    url(r'^viewappointments/patient/(\w+)/', view_appointments_patients, name="ViewAppointmentPatient"),
    url(r'^viewbills/patient/(\w+)/', view_bills_patients, name="ViewBillsPatient"),
    url(r'^settlebill/patient/(\w+)/', settle_bill_patients, name="SettleBillPatient"),
    url(r'^viewappointments/doctor/(\w+)/', view_appointments_doctors, name="ViewAppointmentPatient"),
    url(r'^deleteuser/(\w+)/', delete_user, name="ViewAppointmentPatient"),
    url(r'^testurl/', test_page, name="TestPage"),
    url(r'^validatedoctor/', validate_doctor, name="ValidateDoctor"),
    url(r'^admittedPatients/doctor/(\w+)/', view_Patients, name="ViewPatients"),
    url(r'^viewEarnings/doctor/(\w+)/', view_MonthlyEarnings, name="view_MonthlyEarnings"),
    url(r'^transfer/(\w+)/(\w+)/', transferpatient, name="TransferPatient"),
    url(r'^tconsent/(\w+)/', view_transfer_consents, name="ViewTransferConsent"),
    url(r'^transferapprove/(\w+)/(\w+)/', approve_transfer_consent, name="TransferApprove"),
    url(r'^transferreject/(\w+)/(\w+)/', reject_transfer_consent, name="TransferReject"),
]

