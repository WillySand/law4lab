# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app.models import *
from .serializers import MahasiswaSerializer

class MahasiswaAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = {
                'npm': request.data.get('npm'), 
                'nama': request.data.get('nama'), 
                'alamat': request.data.get('alamat')
            }
            serializer = MahasiswaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"res": "Data is duplicate"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"res": "Data is invalid"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        mahasiswa = Mahasiswa.objects.all()
        serializer = MahasiswaSerializer(mahasiswa, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MahasiswaAPIViewWithID(APIView):
    def get(self, request, npm, *args, **kwargs):
        try:
            mahasiswa = Mahasiswa.objects.get(npm=npm)
            serializer = MahasiswaSerializer(mahasiswa)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"res": "npm does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, npm, *args, **kwargs):
        try:
            data = {
                'nama': request.data.get('nama'), 
                'alamat': request.data.get('alamat')
            }
            mahasiswa = Mahasiswa.objects.get(npm=npm)
            serializer = MahasiswaSerializer(instance=mahasiswa, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"res": "Data is invalid"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TodoSerializer(instance = todo_instance, data=data, partial = True)

    # 5. Delete
    def delete(self, request, npm, *args, **kwargs):
        try:
            mahasiswa = Mahasiswa.objects.get(npm=npm)
            mahasiswa.delete()
            return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
        except:
            return Response({"res": "Object with npm does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        