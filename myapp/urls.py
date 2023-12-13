from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello),
    path('patients/', views.patients, name="patients"),
    path('doctors/', views.doctors, name="doctors"),
    path('doctors/<int:id>', views.doctorDetails, name="doctorDetails"),
    path('patients/<int:id>', views.patientDetails, name="patientDetails"),
    path('doctors/<int:id>/delete', views.eliminarDoctor, name="eliminarDoctor"),
    path('patients/<int:id>/delete', views.eliminarPaciente, name="eliminarPaciente"),
    path('createPatients/', views.createPatients, name="createPatients"),
    path('createDoctors/', views.createDoctors, name="createDoctors"),
]