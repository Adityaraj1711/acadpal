from rest_framework import serializers
from .models import Country, State, City, Town, Person


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


class CountrySerializer(serializers.ModelSerializer):
    """
    A serializer for country details.
    """
    states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['name','description',  'gdp', 'population', 'states']

    def create(self, validated_data):
        states_data = validated_data.pop('states')
        country = Country.objects.create(**validated_data)
        for state_data in states_data:
            State.objects.create(country=country, **state_data)
        return country


class PersonSerializer(serializers.ModelSerializer):
    """A serializer for interest model."""

    class Meta:
        model = Person
        fields = '__all__'
