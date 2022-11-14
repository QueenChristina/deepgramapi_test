from rest_framework import serializers
from rest_framework.serializers import FileField

from .models import Audio

# Turn audio into JSON representation, turn uploaded audio into Audio model
class AudioSerializer(serializers.HyperlinkedModelSerializer):
    file = FileField()
    class Meta:
        model = Audio
        fields = "__all__"
        # fields = ('name', 'duration', 'file', 'title', 'description', 'artist')

class FileUploadSerializer(serializers.Serializer):
    file = FileField()