"""bpkad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pegawai.views import *
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('pegawai/', pegawai, name='pegawai'),
    path('tambah-pegawai/', tambah_pegawai, name='tambah_pegawai' ),
    path('pegawai/ubah/<int:id_pegawai>', ubah_pegawai, name='ubah_pegawai'),
    path('pegawai/hapus/<int:id_pegawai>', hapus_pegawai, name='hapus_pegawai'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup/', signup, name='signup'),
    path('', LoginView.as_view(), name='masuk'),
]
