from django.db import models
from django.contrib.auth.models import User

class Mahasiswa(models.Model):
    nama = models.CharField(max_length = 40)
    alamat = models.CharField(max_length = 40)
    npm = models.CharField(max_length = 40, unique=True)
    
    def __str__(self):
        return self.npm + " - " + self.nama + " - " + self.alamat
