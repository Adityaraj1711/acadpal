from django.shortcuts import render
from django.http import Http404
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Country, State, Town, City, Person
from .serializers import CountrySerializer, StateSerializer, CitySerializer, TownSerializer, PersonSerializer
from .filters import PersonFilter


# Create your views here.
class CountryListViewSet(APIView, PageNumberPagination):
    """Handles reading Country information"""

    def get(self, request, format=None):
        """Returns a list of countries"""
        country = Country.objects.all()
        result = self.paginate_queryset(country, request)
        serializer = CountrySerializer(result, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        country_serializer = CountrySerializer(data=request.data)
        if country_serializer.is_valid():
            country_serializer.save()
            return Response(country_serializer.data, status=status.HTTP_201_CREATED)
        return Response(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            name_error = {"name": ["state name update not allowed"]}
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


class StateListViewSet(APIView, PageNumberPagination):
    """Handles reading state information"""

    def get(self, request, format=None):
        """Returns a list of countries"""
        state = State.objects.all()
        result = self.paginate_queryset(state, request)
        serializer = StateSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateDetailViewSet(APIView):
    """ Perform get, update, delete operation for a state """

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


class CityListViewSet(APIView, PageNumberPagination):
    """Handles reading city information"""

    def get(self, request, format=None):
        """Returns a list of countries"""
        city = City.objects.all()
        result = self.paginate_queryset(city, request)
        serializer = CitySerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDetailViewSet(APIView):
    """ Perform get, update, delete operation for a city """

    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = StateSerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TownListViewSet(APIView, PageNumberPagination):
    """Handles reading town information"""

    def get(self, request, format=None):
        """Returns a list of countries"""
        town = Town.objects.all()
        result = self.paginate_queryset(town, request)
        serializer = TownSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TownDetailViewSet(APIView):
    """ Perform get, update, delete operation for a town """

    def get_object(self, pk):
        try:
            return Town.objects.get(pk=pk)
        except Town.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        town = self.get_object(pk)
        serializer = StateSerializer(town)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        town = self.get_object(pk)
        serializer = StateSerializer(town, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        town = self.get_object(pk)
        town.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonListViewSet(APIView, PageNumberPagination):
    """Handles reading person information"""
    filter_fields = ('name', 'town', 'city', 'town__state__country__name', 'city__state__country__name', 'city__state__name', 'town__state__name')

    def get(self, request, format=None):
        """Returns a list of countries"""
        person = Person.objects.all()
        filter = PersonFilter()
        filtered_queryset = filter.filter_queryset(request, person, self)
        if filtered_queryset.exists():
            result = self.paginate_queryset(person, request)
            serializer = PersonSerializer(result, many=True)
            return Response(serializer.data)
        else:
            return Response([], status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetailViewSet(APIView):
    """ Perform get, update, delete operation for a town """

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


