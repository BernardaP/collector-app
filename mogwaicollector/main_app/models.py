from django.db import models
from datetime import date, time
from django.contrib.auth.models import User
from datetime import datetime

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Mogwai(models.Model):
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()  
    toys = models.ManyToManyField(Toy, blank=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    def no_feeding_after_midnight(self):
        now = datetime.now()
        today_midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_6am = now.replace(hour=5, minute=0, second=0, microsecond=0)
        return not(now >= today_midnight and now < today_6am)
    
    

class Feeding(models.Model):
    date = models.DateField('Feeding date')
    time = models.TimeField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[2][1]
    )
    # Create a mogwai_id FK
    mogwai = models.ForeignKey(Mogwai, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    mogwai = models.ForeignKey(Mogwai, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for mogwai_id: {self.mogwai_id} @{self.url}"
    