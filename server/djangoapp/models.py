from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you'd like here

    def __str__(self):
        return self.name


class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
    ]
    model_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    year = models.DateField()
    # Add any other fields you'd like here

    def __str__(self):
        return f"{self.name} ({self.year})"



# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
