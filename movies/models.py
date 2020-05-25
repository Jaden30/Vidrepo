from django.db import models
from django.utils import timezone

# Create your models here.
# the class enscapulates functionality for storing models in a database
# the class Genre inherits the functionality from django model
class Genre(models.Model): 
    name = models.CharField(max_length = 250)
    #giving it a lemgth enforces it limit

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length = 250)
    release_year = models.IntegerField()
   # continents = models.CharField(max_length = 9)
    showing =  models.CharField(max_length = 50)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    date_created = models.DateTimeField(default =timezone.now) # datetime.now is not a good use
    # because it is not aware of timezone, so instead we use the timezone class in Django.
    def __str__(self):
        return self.title