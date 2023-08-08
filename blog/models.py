from django.db import models
from django.db.models.fields import CharField, TextField, DateField
from django.db.models.fields.files import ImageField
import datetime
# Create your models here.

class Post(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='blog/images')
    date = DateField(datetime.date.today)
