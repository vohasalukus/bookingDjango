from django.contrib.auth.models import User
from django.db import models
from slugify import slugify


class HotelRoom(models.Model):
    room = models.CharField(
        max_length=100
    )
    type = [
        ('S', 'Одноместный номер'),
        ('M', 'Двухместный номер'),
        ('B', 'Трехместный номер')
    ]
    type_of_room = models.CharField(
        max_length=100,
        choices=type
    )
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/rooms'
    )
    slug = models.SlugField(
        unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.room)
        super(HotelRoom, self).save(*args, **kwargs)

    def __str__(self):
        return self.room


class Booking(models.Model):
    entry_date = models.DateField()
    left_date = models.DateField()
    hotel_room = models.ForeignKey(
        HotelRoom,
        on_delete=models.CASCADE,
        related_name='booking'
    )
    user = models.ManyToManyField(
        User,
        related_name='booking'
    )

    def __str__(self):
        return self.hotel_room.room
