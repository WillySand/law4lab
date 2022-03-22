#Check https://www.django-rest-framework.org/api-guide/serializers/
from rest_framework import serializers
from app.models import *

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ['nama', 'alamat', 'npm']