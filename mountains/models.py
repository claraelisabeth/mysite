from django.db import models

class Mountain(models.Model):
    name = models.CharField(max_length=100) # works for short strings and specifies a maximum length
    height = models.IntegerField() # in meters
    country = models.CharField(max_length=100)
    difficulty = models.IntegerField() # number between 1 (easy) and 10 (fucking hardddd)
    comment = models.TextField() # good for longer text - CharField and TextField are built-in model field types (comes with Django)
    first_image = models.FileField(upload_to = "mountain_images/", blank = True)
    detail_image = models.FileField(upload_to = "mountain_images/", blank = True) # blank = True, so it is okay if no pic
