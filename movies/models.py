from django.db import models

# Create your models here.

class Movies(models.Model):
    language_choices = [('Eng', 'English'),
                        ('Beng', 'Bengali'),
                        ('Span', 'Spanish'),
                        ('Fre', 'French')]
    movie_name = models.CharField(max_length=255, unique=True)
    director = models.CharField()
    released_year = models.IntegerField()
    story = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=4)
    language = models.CharField(choices=language_choices)
    


class Rating(models.Model):
    reviewer = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    rating = models.FloatField()
    movie = models.ForeignKey(Movies, related_name='ratings', on_delete=models.CASCADE)

