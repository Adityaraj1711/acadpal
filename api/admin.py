from django.contrib import admin
from .models import Country, State, City, Town, Person


class CountryAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(CountryAdmin, self).get_readonly_fields(request, obj)
        if obj:  # editing an existing object
            return readonly_fields + ('description', 'gdp')
        return readonly_fields


# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Town)
admin.site.register(Person)
