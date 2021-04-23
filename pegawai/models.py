from django.db import models


# Create your models here.
class pangkat(models.Model):
    gol = models.CharField(max_length=6)
    pangkat = models.CharField(max_length=20)

    def __str__(self):
        return self.gol


class pegawai(models.Model):
    nip = models.CharField(max_length=18)
    nama = models.CharField(max_length=25)
    jabatan = models.CharField(max_length=50)
    pangkat = models.ForeignKey(pangkat, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.nip
