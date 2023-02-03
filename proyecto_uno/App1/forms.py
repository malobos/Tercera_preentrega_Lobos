from django import forms

class frecCarne(forms.Form):
    nombre= forms.CharField()
    fechaDeSubida= forms.DateField()
    ingredientes= forms.CharField()
class frecVerduras(forms.Form):
    nombre= forms.CharField()
    fechaDeSubida= forms.DateField()
    ingredientes= forms.CharField()
class frecPastas(forms.Form):
    nombre= forms.CharField()
    fechaDeSubida= forms.DateField()
    ingredientes= forms.CharField()
class fcontacto(forms.Form):
    nombre= forms.CharField()
    apellido=forms.CharField()
    correo = forms.EmailField() 
