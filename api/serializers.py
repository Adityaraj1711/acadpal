from rest_framework import serializers
from .models import Country, State, City, Town, Person


class CountrySerializer(serializers.ModelSerializer):
    """
    A serializer for country details.
    """
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    """A serializer for college details."""

    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    """A serializer for interest model."""

    class Meta:
        model = City
        fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
    """A serializer for interest model."""

    class Meta:
        model = Town
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    """A serializer for interest model."""

    class Meta:
        model = Person
        fields = '__all__'
