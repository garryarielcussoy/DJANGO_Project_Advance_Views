from django.db import models

# Create your models here.
class Blog(models.Model):
    foto = models.CharField(max_length=255, default="")
    waktu_publikasi = models.DateField("Waktu Tayang")
    jumlah_komentar = models.IntegerField(default=0)
    judul_post = models.CharField(max_length=255, default="")
    konten = models.TextField(default="")

    def __str__(self):
        return self.judul_post

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255, default="")
    foto = models.CharField(max_length=255, default="")
    testimoni = models.TextField(default="")

    def __str__(self):
        return self.nama_lengkap

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255, default="")
    foto = models.CharField(max_length=255, default="")
    pengalaman = models.TextField(default="")
    testimoni = models.TextField(default="")

    def __str__(self):
        return self.nama_lengkap