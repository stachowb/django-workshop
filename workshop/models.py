from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField(default=0)
    projector = models.BooleanField(default=False)


class Reservations(models.Model):
    reserved_from = models.DateTimeField()
    reserved_until = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=None)


class Equipment(models.Model):
    name=models.CharField(max_length=64)
    available = models.BooleanField(default=True)
    room = models.ManyToManyField(Room)


