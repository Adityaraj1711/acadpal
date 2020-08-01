from django.contrib import admin
from .models import Country, State, City, Town, Person


class CountryAdmin(admin.ModelAdmin):
    readonly_fields=('name',)


# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Town)
admin.site.register(Person)
