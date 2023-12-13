from django import forms

class createNewPatient(forms.Form):
    name = forms.CharField(label="Nombre del paciente")
    age = forms.IntegerField(label="Edad")
    phone = forms.IntegerField(label="Telefono")

class createNewDoctor(forms.Form):
    name = forms.CharField(label="Nombre del doctor")
    age = forms.IntegerField(label="Edad")
    phone = forms.IntegerField(label="Telefono")
    location = forms.CharField(widget=forms.Textarea, label="Ubicación")

class DoctorsForm(forms.Form):
    name = forms.CharField(label="Nombre del doctor")
    age = forms.IntegerField(label="Edad")
    phone = forms.IntegerField(label="Telefono")
    location = forms.CharField(widget=forms.Textarea, label="Ubicación")
    # Add other form fields corresponding to your model fields...

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(DoctorsForm, self).__init__(*args, **kwargs)

        # If an instance is provided, populate the form with its data
        if instance:
            for field in self.fields:
                self.fields[field].initial = getattr(instance, field, None)

class PatientForm(forms.Form):
    name = forms.CharField(label="Nombre del paciente")
    age = forms.IntegerField(label="Edad")
    phone = forms.IntegerField(label="Telefono")
    # Add other form fields corresponding to your model fields...

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(PatientForm, self).__init__(*args, **kwargs)

        # If an instance is provided, populate the form with its data
        if instance:
            for field in self.fields:
                self.fields[field].initial = getattr(instance, field, None)
