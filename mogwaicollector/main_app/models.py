from django.db import models

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Mogwai(models.Model):
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()    

    def __str__(self):
        return f"{self.name}"

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