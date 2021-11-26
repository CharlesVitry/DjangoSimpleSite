from django.db import models

# Create your models here.
class User(models.Model):
    identifiant = models.IntegerField()
    motdepasse = models.CharField(max_length=8)
    professeur = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.identifiant}'

