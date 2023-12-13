from django.http import HttpResponse, JsonResponse
from .models import Doctors, Patients
from django.shortcuts import get_object_or_404, render, redirect
from .forms import createNewPatient, createNewDoctor, DoctorsForm, PatientForm

def index(request):
    name = ' a Doctoradar'
    return render(request, 'index.html', {
        'name': name
    })

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    print(username)
    return HttpResponse("Hello %s" % username)

def doctors(request):
    # doctor = list(Doctors.objects.values())
    doctors = Doctors.objects.all()
    return render(request, 'doctors.html', {
        'doctors': doctors
    })

def patients(request):
    # patient = get_object_or_404(Patients, id=id)
    patients = Patients.objects.all()
    return render(request, 'patients.html', {
        'patients': patients
    })

def createPatients(request):
    if request.method == 'GET':
        return render(request, 'createPatients.html', {
        'form': createNewPatient()
        }) 
    else:
         Patients.objects.create(name=request.POST['name'], age=request.POST['age'], phone=request.POST['phone'], doctor_id=1)
         return redirect('patients')

def createDoctors(request):
    if request.method == 'GET':
        return render(request, 'createDoctors.html', {
        'form': createNewDoctor()
        })
    else:
        Doctors.objects.create(name=request.POST['name'], age=request.POST['age'], phone=request.POST['phone'], location=request.POST['location'])
        return redirect('doctors')

def doctorDetails(request, id):
    doctor = get_object_or_404(Doctors, id=id)

    if request.method == 'POST':
        form = DoctorsForm(request.POST)
        if form.is_valid():
            # Update the instance with the form data
            doctor.name = form.cleaned_data['name']
            doctor.age = form.cleaned_data['age']
            doctor.phone = form.cleaned_data['phone']
            doctor.location = form.cleaned_data['location']
            # Update other fields accordingly...

            doctor.save()
            return redirect('doctors')
            # Handle form submission success, e.g., redirect to another page
    else:
        form = DoctorsForm(instance=doctor)

    return render(request, 'doctorDetails.html', {
        'doctor': doctor,
        'form': form
    })

def patientDetails(request, id):
    patient = get_object_or_404(Patients, id=id)

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            # Update the instance with the form data
            patient.name = form.cleaned_data['name']
            patient.age = form.cleaned_data['age']
            patient.phone = form.cleaned_data['phone']
            # Update other fields accordingly...

            patient.save()
            return redirect('patients')
            # Handle form submission success, e.g., redirect to another page
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patientDetails.html', {
        'patient': patient,
        'form': form
    })

def eliminarDoctor(request, id):
    doctor = get_object_or_404(Doctors, id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors')
    

def eliminarPaciente(request, id):
    patient = get_object_or_404(Patients, id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients')
