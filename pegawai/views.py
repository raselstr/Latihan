from django.shortcuts import render
from pegawai.models import Pegawai
from pegawai.forms import FormPegawai
# Create your views here.

def pegawai(request):
    pgws = Pegawai.objects.all()  # menampilan seluruh data tabel
    # pgws = Pegawai.objects.filter(pangkat__pangkat = "Pengatur Tk. 1") #Menggunakan Filter pangkat dengan menampilkan nama pangkat dari Model Pangkat
    # pgws = Pegawai.objects.filter(pangkat__pangkat = "Pengatur Tk. 1") [:3] # [:3] Limit

    konteks = {
        'pgws':pgws,
        
    }
    return render(request, 'pegawai.html', konteks)


def tambah_pegawai(request):
    if request.POST:
        form = FormPegawai(request.POST)
        if form.is_valid():
            form.save()
            form = FormPegawai()
            pesan = "Data berhasil ditambah"

            konteks = {
                'form': form,
                'pesan' : pesan,
            }

            return render(request, 'tambah-pegawai.html', konteks)
     
    else:

        form = FormPegawai()

        konteks = {
            'form' : form,
        }

        return render(request, 'tambah-pegawai.html', konteks)