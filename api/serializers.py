from rest_framework import serializers

from .models import Audio

# Turn audio into JSON representation, turn uploaded audio into Audio model
class AudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"
        # fields = ('name', 'duration', 'file', 'title', 'description', 'artist') # Synonymous to __all__