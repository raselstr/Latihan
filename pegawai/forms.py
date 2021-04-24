from django.forms import ModelForm
from django import forms
from pegawai.models import Pegawai

class FormPegawai(ModelForm):
    class Meta:
        model = Pegawai
        fields = '__all__' #menampilkan semua field
        # exclude = ['pangkat'] # exclude = Kecuali

        widgets = {
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'pangkat' : forms.Select({'class':'form-control'}),
        }
