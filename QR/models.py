from django.db import models

# Create your models here.
import pyqrcode
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile


class StaffInfo(models.Model):
    staff_name = models.CharField(max_length=255)
    staff_id = models.IntegerField(max_length=255)   
    staff_position = models.CharField(max_length=255)
    staff_department = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super(StaffInfo, self).save(*args, **kwargs)
        qr = pyqrcode.create(self.staff_id)
        qr.png("qrcode/"+self.staff_name+".png", scale=30)
        
    def __str__(self):
        return self.staff_name  
         