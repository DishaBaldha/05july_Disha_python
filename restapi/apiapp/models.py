from django.db import models
from datetime import datetime

# Create your models here.

class patient(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
# Create your models here.
