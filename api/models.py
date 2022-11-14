from django.db import models

from tinytag import TinyTag

# Create your models here.
class Audio(models.Model):
    name = models.CharField(max_length=60, blank=True)
    duration = models.IntegerField(blank=True, null=True) # seconds
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=60, blank=True, null=True)
    artist = models.CharField(max_length=60, blank=True, null=True)
    filesize = models.IntegerField(blank=True, null=True) # bytes
    bitrate = models.IntegerField(blank=True, null=True) # kBits/s

    def save(self, *args, **kwargs):
        self.name = self.file.name
        audio = TinyTag.get(self.file.file.temporary_file_path())
        self.duration = audio.duration
        self.artist = audio.artist
        self.title = audio.title
        self.filesize = audio.filesize
        self.bitrate = audio.bitrate
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name