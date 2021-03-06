from django.db import models


# Create your models here.
class Country(models.Model):
    """Represents a "Country model". Stores all country GDP and population
    related data"""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()

    def __str__(self):
        """Return the model as a string."""

        return self.name


class State(models.Model):
    """Represents a "State model". Stores GDP and population of each state for each country """

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()

    def __str__(self):
        """Return the model as a string."""
        return self.name


class City(models.Model):
    """Represents a "City model". Stores GDP, description and population of each city for each state """

    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        """Return the model as a string."""

        return self.description


class Town(models.Model):
    """Represents a "Town model". Stores GDP, description and population of each town for each state """

    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='towns')
    description = models.TextField()
    population = models.IntegerField()
    gdp = models.FloatField()
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        """Return the model as a string."""

        return self.description


class Person(models.Model):
    name = models.CharField(max_length=100, default='')
    town = models.ForeignKey(Town, on_delete=models.PROTECT, related_name='townperson', null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='cityperson', null=True)

    def __str__(self):
        return self.name
