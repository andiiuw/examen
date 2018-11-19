from django import forms
from .models import *

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ('numero','capacidad' ,'responsable')

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('nombre','formato','duracion')

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ('pelicula','destinatario','direccion','descripcion')

class CiudadForm(forms.ModelForm):

    class Meta:
        model = Ciudad
        fields = ('sala','pelicula')

        def __init__ (self, *args, **kwargs):
            super(CiudadForm, self).__init__(*args, **kwargs)
            self.fields["pelicula"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["pelicula"].help_text = "Ingrese las peliculas"
            self.fields["pelicula"].queryset = Paquete.objects.all()
