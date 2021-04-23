from django.shortcuts import render
from pegawai.models import Pegawai
# Create your views here.

def pegawai(request):
    pgws = Pegawai.objects.all()
    

    konteks = {
        'pgws':pgws,
        
    }
    return render(request, 'pegawai.html', konteks)