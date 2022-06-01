from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Anime(models.Model):
        name = models.CharField(max_length=300)
        episodes = models.IntegerField()
        def get_absolute_url(self):
            return f"/anime/{self.pk}"

        def __str__ (self):
            return self.name

class Yamanian(models.Model):
    nickname = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    age = models.IntegerField()
    anime = models.ManyToManyField('Anime')
    about = models.TextField()
    membership = models.BooleanField(default = True)
    
    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f"/yamanians/{self.pk}"
        
class Comment(models.Model):
        title = models.CharField(max_length=250)
        text = models.TextField()
        name = models.ForeignKey(User, on_delete=models.CASCADE)
        anime = models.ForeignKey('Anime', on_delete=models.CASCADE)





        

