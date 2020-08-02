from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import CountryListViewSet, CountryDetailViewSet, StateListViewSet, StateDetailViewSet


urlpatterns = [
    path("country/", CountryListViewSet.as_view(), name="country_list"),
    path("country/<int:pk>", CountryDetailViewSet.as_view(), name="country_detail"),
    path("state/", StateListViewSet.as_view(), name="country_list"),
    path("state/<int:pk>", StateDetailViewSet.as_view(), name="country_detail"),
]