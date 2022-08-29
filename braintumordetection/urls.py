"""braintumordetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static

from braintumordetection import settings
from patients import views as patients_views
from doctors import  views as doctors_views

urlpatterns = [
    url('admin/', admin.site.urls),

url(r'^$',patients_views.userlogin, name="userlogin"),
url(r'^register$',patients_views.register, name="register"),
url(r'^myaccounts',patients_views.myaccounts, name="myaccounts"),
url(r'^doctorview',patients_views.doctorview, name="doctorview"),
url(r'^feedback',patients_views.feedback, name="feedback"),
url(r'^patientslogout',patients_views.patientslogout, name="patientslogout"),
url(r'^select_image$',patients_views.select_image, name="select_image"),
url(r'^Postmriimage$',patients_views.Postmriimage, name="Postmriimage"),



url(r'^adminlogin', doctors_views.adminlogin, name="adminlogin"),
url(r'^adddoctor', doctors_views.adddoctor, name="adddoctor"),
url(r'^patientsdetails', doctors_views.patientsdetails, name="patientsdetails"),
url(r'^viewdoctors', doctors_views.viewdoctors, name="viewdoctors"),
url(r'^patientsreviews', doctors_views.patientsreviews, name="patientsreviews"),
url(r'^tumourscan', doctors_views.tumourscan, name="tumourscan"),
url(r'^viewMRIimage', doctors_views.viewMRIimage, name="viewMRIimage"),
url(r'^adminlogout', doctors_views.adminlogout, name="adminlogout"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
