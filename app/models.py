from django.db import models

class Image(models.Model):
    img = models.FileField(null=False, blank=False, upload_to='media/')
    
    def __str__(self):
        return str(f"{self.img.url}")
