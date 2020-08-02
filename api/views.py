from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Country, State, Town, City, Person
from .serializers import CountrySerializer, StateSerializer, CitySerializer, TownSerializer, PersonSerializer


# Create your views here.
class CountryListViewSet(APIView):
    """Handles reading Country information"""

    def get(self, request, format=None):
        """Returns a list of countries"""
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryDetailViewSet(APIView):
    """ Perform get, update, delete operation for country """

    def get_object(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        country = self.get_object(pk)
        print(country.name)
        serializer = CountrySerializer(country, data=request.data)
        if 'name' in request.data and not country.name == request.data['name']:
            name_error = {"name": ["country name update not allowed"]}
            return Response(name_error, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        country = self.get_object(pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StateListViewSet(APIView):
    """Handles reading state information"""

    def get(self, request, format=None):
        """Returns a list of countries"""
        state = State.objects.all()
        serializer = CountrySerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateDetailViewSet(APIView):
    """ Perform get, update, delete operation for country """

    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        state = self.get_object(pk)
        serializer = StateSerializer(state)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        state = self.get_object(pk)
        print(state.name)
        serializer = StateSerializer(state, data=request.data)
        if 'name' in request.data and not state.name == request.data['name']:
            name_error = {"name": ["country name update not allowed"]}
            return Response(name_error, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        state = self.get_object(pk)
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

