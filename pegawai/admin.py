from django.contrib import admin
from pegawai.models import pegawai, pangkat
# Register your models here.

class PegawaiAdmin(admin.ModelAdmin):
    list_display = ['nip','nama','jabatan','pangkat']
    search_fields = ['nama','jabatan']
    list_filter = ('pangkat',)
    list_per_page = 5

admin.site.register(pegawai, PegawaiAdmin)
admin.site.register(pangkat)

