from django.shortcuts import render

# Create your views here.

def pegawai(request):
    nama = ["budi", "anto", "iwan"]
    alamat = "air joman"

    konteks = {
        'nama':nama,
        'alamat':alamat,
    }
    return render(request, 'pegawai.html', konteks)