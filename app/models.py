from django.db import models

class Movie(models.Model):
    title = models.TextField()
    rating = models.IntegerField()
    genre = models.TextField()
    runtime = models.CharField()

class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtime = models.TimeField()

class Ticket(models.Model):
    name = models.TextField()
    purchased_at = models.DateTimeField()
    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)