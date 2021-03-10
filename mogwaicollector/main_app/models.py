from django.db import models
from datetime import date

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

    def __str__(self):
        return f"{self.name}"

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('Feeding date')
    # time = models.TimeField()
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