from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import AudioSerializer
from .models import Audio

from pathlib import Path

class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all().order_by('name')
    serializer_class = AudioSerializer

    def create(self, request, format=None):
        serializer = AudioSerializer(data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle different queries and filters
    def list(self, request):
        queryset = Audio.objects.all().order_by('name')
        # Filter on duration
        maxduration = self.request.query_params.get('maxduration')
        if maxduration is not None:
            queryset = queryset.filter(duration__lte=maxduration)
        minduration = self.request.query_params.get('minduration')
        if minduration is not None:
            queryset = queryset.filter(duration__gte=minduration)
        # Filter on name
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)

        # Filter by parameters, increasing
        if self.request.query_params.get('upload_time') is not None:
            queryset = queryset.order_by('uploaded_at')
        if self.request.query_params.get('size') is not None:
            queryset = queryset.order_by('filesize')
        if self.request.query_params.get('duration') is not None:
            queryset = queryset.order_by('duration')
        if self.request.query_params.get('bitrate') is not None:
            queryset = queryset.order_by('bitrate')

        serializer = AudioSerializer(queryset, many=True, context = {'request': request})
        return Response(serializer.data)