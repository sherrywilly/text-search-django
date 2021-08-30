from django.db import models

# Create your models here.
class Video(models.Model):
    youtube_id = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title
class User(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return self.fname
    