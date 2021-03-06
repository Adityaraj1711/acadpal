from rest_framework import serializers
from .models import Country, State, City, Town, Person


class PersonSerializer(serializers.ModelSerializer):
    """A serializer for person model."""

    class Meta:
        model = Person
        fields = '__all__'
        depth = 3


class CitySerializer(serializers.ModelSerializer):
    """A serializer for city model."""
    cityperson = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = '__all__'
        depth = 1


class TownSerializer(serializers.ModelSerializer):
    """A serializer for town model."""
    townperson = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Town
        fields = '__all__'
        depth = 1


class StateSerializer(serializers.ModelSerializer):
    """A serializer for state details."""
    cities = CitySerializer(many=True, read_only=True)
    towns = TownSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['id', 'name', 'description', 'gdp', 'population', 'country', 'cities', 'towns']


class CountrySerializer(serializers.ModelSerializer):
    """
    A serializer for country details.
    """
    states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'description',  'gdp', 'population', 'states']

    # def create(self, validated_data):
        # states_data = validated_data.pop('states')
        # country = Country.objects.create(**validated_data)
        # for state_data in states_data:
        #     State.objects.create(country=country, **state_data)
        # return country

