from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False)
    age = models.IntegerField()
    gender = models.CharField(blank=False, max_length=10)
    phone = models.IntegerField(default=1)


def __str__(self):
    return self.name
