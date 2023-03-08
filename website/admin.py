from django.contrib import admin
from .models import *

@admin.register(DateAndLocation)
class DateAdmin(admin.ModelAdmin):
	list_display = ('date','latitude', 'longitude', 'city', 'state')
	ordering = ('date','latitude', 'longitude', 'city', 'state')
	search_fields = ('date','latitude', 'longitude', 'city', 'state')

@admin.register(ClimateFactor)
class ClimateAdmin(admin.ModelAdmin):
	list_display = ('maxTemp', 'minTemp', 'avgTemp', 'avgWindSpeed', 'avgPrecipitation', 'research', 'date')
	ordering = ('maxTemp', 'minTemp', 'avgTemp', 'avgWindSpeed', 'avgPrecipitation', 'research', 'date')
	search_fields = ('maxTemp', 'minTemp', 'avgTemp', 'avgWindSpeed', 'avgPrecipitation', 'research', 'date')

@admin.register(Concentration)
class ConcentrationAdmin(admin.ModelAdmin):
	list_display = ('concentration', 'date')
	ordering = ('concentration', 'date')
	search_fields = ('concentration', 'date')

