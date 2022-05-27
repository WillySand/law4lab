# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app.models import *
from .serializers import MahasiswaSerializer
import os
import environ
import json
import requests

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
            env = environ.Env()
            environ.Env.read_env()
            api_key = (os.environ.get("APIKEY_LOG", '1111'))
            url = "https://b5e73130-42e3-4c1a-9149-bc23fd8b4ed1-es.logit.io/log*/_search/?apikey="+api_key
            payload = '{"size":20,"sort":[{"@timestamp":{"order":"desc","unmapped_type":"boolean"}}],"aggs":{"2":{"date_histogram":{"field":"@timestamp","fixed_interval":"30m","time_zone":"Asia/Bangkok","min_doc_count":1}}},"query":{"bool":{"must":[],"filter":[{"match_all":{}}]}}}'
            res = requests.post(headers={"content-type":"application/json"})
            log_json = json.loads(res.text)
            logs=[]
            if (not log_json['timed_out']):
                for i in log_json['hits']['hits']:
                    logs.append(i['_source'])
            return Response({"res":logs}, status=status.HTTP_400_BAD_REQUEST)

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
        
