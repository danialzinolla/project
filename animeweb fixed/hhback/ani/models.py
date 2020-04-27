from django.db import models

class Anime(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField(default=7.7)
    description = models.TextField(default='')
    image = models.TextField(default='')

class Anime_wsite(models.Model):
    name = models.CharField(max_length=100)
    ani_url = models.TextField(default='')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)


class Simi_anime(models.Model):
    name = models.CharField(max_length=100)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)


class Koment(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(default='')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
