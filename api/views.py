from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import AudioSerializer
from .models import Audio
# from rest_framework.parsers import FileUploadParser
from .serializers import FileUploadSerializer

from pathlib import Path

class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all().order_by('name')
    serializer_class = AudioSerializer
    # parser_classes = [FileUploadParser]

    # @action(detail=False)
    # def recent_audio(self, request):
    #     recent_audio = Audio.objects.all().order_by('uploaded_at')

    #     page = self.paginate_queryset(recent_audio)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(recent_audio, many=True)
    #     return Response(serializer.data)


    def create(self, request, format=None):
        print("POSTING ATTEMPT")
        print(request.data)
        print(request.FILES)
        print("Data file", request.data.get('file'))
        if request.data.get('file'):
            # request_file = request.data.get('file')
            # print(request_file)
            # # file = File(docfile=request_file, title='something')
            # file_path = request_file.save()
            # Audio.file = file_path
            print("GOT FILE")
            file_path = request.data.get('file')
            # _file = file_path.save()

            # _file = open(file_path, 'rb')
            # request.data.file = _file

            # request.data = {'file': _file}
            # instance = Audio.objects.create(file=open(file_path, 'rb'))

            # file_uploaded = request.data.get('file')
            # response = "POST API and you have uploaded a {} file".format(file_uploaded)
            # return Response(response)
            # print(instance)

            # print(_file)
            # print("FILE MADE")
            # _file.close()
        else:
            print("NO FILE")
            return Response(dict(error="No audio file uploaded"), status=status.HTTP_400_BAD_REQUEST)
        
        # serializer = FileUploadSerializer(data=request.data)
        serializer = AudioSerializer(data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("NO FILE 2")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle different queries and filter
    def get_queryset(self):
        queryset = Audio.objects.all().order_by('name')
        maxduration = self.request.query_params.get('maxduration')
        if maxduration is not None:
            queryset = queryset.filter(duration__level__lte=maxduration)
        if self.request.query_params.get('recent') is not None:
            queryset = queryset.order_by('uploaded_at')
        if self.request.query_params.get('size') is not None:
            queryset = queryset.order_by('filesize')
        if self.request.query_params.get('duration') is not None:
            queryset = queryset.order_by('duration')
        minduration = self.request.query_params.get('minduration')
        if minduration is not None:
            queryset = queryset.filter(duration__level__gte=minduration)
        return queryset