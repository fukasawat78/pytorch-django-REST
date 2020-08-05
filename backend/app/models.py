from django.db import models
import jsonfield

class ImageModel(models.Model):
    name = models.CharField(max_length = 128, null=True, default="unknown")
    image = models.ImageField(upload_to="media")
    predict = jsonfield.JSONField
