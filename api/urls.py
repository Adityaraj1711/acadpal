from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import CountryListViewSet, CountryDetailViewSet, \
    StateListViewSet, StateDetailViewSet, \
    CityListViewSet, CityDetailViewSet, \
    TownListViewSet, TownDetailViewSet


urlpatterns = [
    path("country/", CountryListViewSet.as_view(), name="country_list"),
    path("country/<int:pk>", CountryDetailViewSet.as_view(), name="country_detail"),
    path("state/", StateListViewSet.as_view(), name="state_list"),
    path("state/<int:pk>", StateDetailViewSet.as_view(), name="state_detail"),
    path("city/", CityListViewSet.as_view(), name="city_list"),
    path("city/<int:pk>", CityDetailViewSet.as_view(), name="city_detail"),
    path("town/", TownListViewSet.as_view(), name="town_list"),
    path("town/<int:pk>", TownDetailViewSet.as_view(), name="town_detail"),

]