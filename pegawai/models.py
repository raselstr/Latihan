from django.db import models

# Create your models here.
class pegawai(models.Model):
    nip = models.CharField(max_length=18)
    nama = models.CharField(max_length=25)
    jabatan = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nip
