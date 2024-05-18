from django.db import models

class File(models.Model):
    # file = models.FileField(upload_to='files/')
    file_name = models.CharField(max_length=255)
    size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)